from ftl.internal.interface import (
    STEP, FIELDSET
)
from ftl.internal.standardized_actions import (
    UPDATE, UPDATE_FOR_CONFIRMATION, RESEND_OTP
)
from ftl.internal.standardized_fields import (
    INFO, ERROR, STRING, RADIO_CHOICE
)


def OTP(
    step_type="form",
    title="Εισαγωγή κωδικού επιβεβαίωσης",
    next_step="final_view",
    validator="dilosi.interop_logic.common.run_otp_response",
    **kwargs,
):
    HINT_FS = FIELDSET(
        fieldset_name="hint",
        fields=[
            STRING(
                "hint_text", None, "noinput", "hidden",
                value="Σας έχει σταλεί με SMS κωδικός επιβεβαίωσης στο κινητό με αριθμό %s.\nΠαρακαλούμε συμπληρώστε τον κωδικό στο πεδίο που ακολουθεί."
            ),
            STRING(
                "hint_text_filled", user_input_mode="display",
                sources="displayfield:hint_text declaration:id",
                value_constructor="dilosi.interop_logic.otp_challenge.fill_otp_hint_text",
            ),
        ]
    )

    OTP_FS = FIELDSET(
        fieldset_name="otp",
        fields=[
            STRING("otp_challenge_id", None, "noinput", "hidden", "otp_challenge:id"),
            STRING("confirmation_code", "Κωδικός Επιβεβαίωσης"),
        ],
        title="Στοιχεία Πολίτη",
    )
    kwargs["fieldsets"] = [HINT_FS, OTP_FS]
    kwargs["actions"] = [
        UPDATE_FOR_CONFIRMATION(),
        RESEND_OTP(),
    ]
    OTP_STEP = STEP(
        step_type=step_type,
        title=title,
        next_step=next_step,
        validator=validator,
        **kwargs,
    )

    return OTP_STEP


def CONSENT_METHOD(
    step_type="form",
    actions=[UPDATE()],
    title="Επιλέξτε τον τρόπο με τον οποίο θα δώσετε επιβεβαίωση έκδοσης του εγγράφου.",
    next_step=(
        "dilosi.applications.gov_wallet.claims.common.get_otp_or_gov_wallet_method_step",
        ("gov_wallet_method", "otp")
    ),
    validator="dilosi.interop_logic.common.consent_response",
    **kwargs,
):

    INFO_FS = FIELDSET(
        fieldset_name="info_fs",
        fields=[
            INFO(
                "gov_wallet_method_info",
                safe=True,
                sources="declaration:user_id",
                value_constructor="dilosi.applications.gov_wallet.claims.common.get_gov_wallet_method_info",
            ),
            ERROR(
                "previous_attempt_info",
                sources="field:previous_attempt",
                value_constructor="dilosi.applications.gov_wallet.claims.common.get_previous_attempt_info",
            ),
        ],
        params={"omit_empty_values": True}
    )

    CONSENT_METHOD_FS = FIELDSET(
        fieldset_name="consent_method_fs",
        fields=[RADIO_CHOICE(
            "consent_method",
            choices_source_fn="dilosi.applications.gov_wallet.claims.common.get_consent_method_choices"
        )]
    )

    CONSENT_METHOD_STEP = STEP(
        step_type=step_type,
        title=title,
        actions=actions,
        fieldsets=[INFO_FS, CONSENT_METHOD_FS],
        next_step=next_step,
        **kwargs,
    )

    return CONSENT_METHOD_STEP


def GOV_WALLET(
    step_type="form",
    actions=[UPDATE_FOR_CONFIRMATION(
        issue=False,
        autocall=True,
        retry={
            'retry_limit': 30,
            'retry_delay': 1000,
        },
        poll={
            'id_field': 'poll_id',
            'retry/retry_limit': 120,
            'retry/retry_delay': 1000,
            'endpoint': 'validation/consent_status',
        }
    )],
    title="Αναμονή αποδοχής αιτήματος.",
    next_step=(
        "dilosi.applications.gov_wallet.claims.common.check_consent_maybe_get_next_step",
        ("consent_method", "rejected", "final_view")
    ),
    **kwargs,
):

    HINT_FS = FIELDSET(
        fieldset_name="hint",
        fields=[
            STRING(
                "gov_wallet_request_id", None, "noinput", "hidden",
                "gov_wallet_issue_consent_request:request_id"
            ),
            STRING(
                "poll_id", None, "noinput", "hidden",
                sources="declaration:id"
            ),
            STRING(
                "hint_text", None, "noinput", "hidden",
                value="Αναμονή επιβεβαίωσης μέσω Gov.gr Wallet με κωδικό %s."
            ),
            STRING(
                "hint_text_filled", user_input_mode="display",
                sources="displayfield:hint_text declaration:id",
                value_constructor="dilosi.applications.gov_wallet.claims.gov_wallet_issue_consent_request.fill_gov_wallet_consent_hint_text",
            ),
        ]
    )

    GOV_WALLET_STEP = STEP(
        step_type=step_type,
        title=title,
        actions=actions,
        fieldsets=[HINT_FS],
        next_step=next_step,
        field_compute_order="gov_wallet_request_id",
        **kwargs,
    )

    return GOV_WALLET_STEP


def REJECTED(
    step_type="form",
    actions=[],
    title=None,
    next_step=None,
    **kwargs,
):

    REJECTED_FS = FIELDSET(
        fieldset_name="rejected_fs",
        fields=[
            STRING(
                "rejected_consent_id", None, "noinput", "hidden",
                "gov_wallet_issue_consent_response:consent_id"
            ),
            ERROR("rejected_field", value="Το αίτημα απορρίφθηκε"),
        ]
    )

    REJECTED_STEP = STEP(
        step_type=step_type,
        title=title,
        actions=actions,
        fieldsets=[REJECTED_FS],
        next_step=next_step,
        **kwargs,
    )

    return REJECTED_STEP


def CONSENT_METHOD_STEPS(
    next_step=(
        "dilosi.applications.gov_wallet.claims.common.check_consent_maybe_get_next_step",
        ("consent_method", "rejected", "final_view")
    ),
):
    after_consent_step = next_step[1][-1]
    return [
        CONSENT_METHOD(),
        OTP(
            validator="dilosi.interop_logic.common.consent_response",
            next_step=after_consent_step,
        ),
        GOV_WALLET(next_step=next_step),
        REJECTED(),
    ]
