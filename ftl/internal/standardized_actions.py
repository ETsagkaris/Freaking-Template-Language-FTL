from ftl.internal.interface import (
    ACTION as action_shell, get_obj_interface
)

action_interface = get_obj_interface(action_shell)


@action_interface()
def ACTION(kwargs):
    return kwargs


@action_interface(
    action_name="update",
    component="document-update",
    label="Συνέχεια",
    primary=True
)
def UPDATE(kwargs):
    return kwargs


@action_interface(
    action_name="update",
    component="document-update",
    label="Έκδοση",
    primary=True,
    ensure_no_input=True
)
def UPDATE_FOR_REQUEST(kwargs):
    return kwargs


@action_interface(
    action_name="update",
    component="document-update",
    label="Επιβεβαίωση",
    primary=True,
    issue=True,
    ensure_no_input=False
)
def UPDATE_FOR_CONFIRMATION(kwargs):
    return kwargs


@action_interface(
    action_name="update",
    component="document-update",
    label="Έκδοση",
    primary=True,
    issue=True,
    ensure_no_input=True
)
def UPDATE_FOR_SUBMISSION(kwargs):
    return kwargs


@action_interface(
    action_name="update",
    component="document-collect",
    label="Συνέχεια",
    primary=True
)
def COLLECT(kwargs):
    return kwargs


@action_interface(
    action_name="update",
    component="document-issue-collected",
    label="Έκδοση",
    primary=True,
    issue=True
)
def ISSUE_COLLECTED(kwargs):
    return kwargs


@action_interface(
    action_name="backstep",
    component="document-backstep",
    label="Πίσω",
    primary=False
)
def BACKSTEP(kwargs):
    return kwargs


@action_interface(
    action_name="share",
    component="document-share",
    label="Κοινοποίηση",
    primary=False,
    title="Κοινοποιήστε το έγγραφο",
    helptext="Κοινοποιήστε το έγγραφο στη θυρίδα άλλου πολίτη."
)
def SHARE(kwargs):
    return kwargs


@action_interface(
    action_name="resend_otp",
    component="document-resend-otp",
    label="Δεν έλαβα κωδικό",
    primary=False
)
def RESEND_OTP(kwargs):
    return kwargs


@action_interface(
    action_name="resend_email_otp",
    component="document-resend-email-otp",
    label="Δεν έλαβα κωδικό",
    primary=False
)
def RESEND_EMAIL_OTP(kwargs):
    return kwargs


@action_interface(
    action_name="sms",
    component="document-sms",
    label="Αποστολή SMS",
    primary=False,
    title="Λάβετε το έγγραφο μέσω SMS",
    helptext="Λάβετε το έγγραφο μέσω SMS στον αριθμό τηλεφώνου που δηλώσατε."
)
def SMS(kwargs):
    return kwargs


@action_interface(
    action_name="email",
    component="document-email",
    label="Αποστολή E-mail",
    primary=False,
    title="Λάβετε το έγγραφο μέσω E-mail",
    helptext="Λάβετε το έγγραφο στη διεύθυνση ηλεκτρονικού ταχυδρομείου σας."
)
def EMAIL(kwargs):
    return kwargs


@action_interface(
    action_name="communication",
    component="entity-send-message",
    label="Αποστολή μηνύματος",
    primary=False,
    contact_phone_field="mobile",
    contact_email_field="email",
)
def COMMUNICATION(kwargs):
    return kwargs


@action_interface(
    action_name="temporary-save",
    component="document-temporary-save",
    label="Προσωρινή Αποθήκευση",
    primary=False,
    url="/vault/drafts",
    is_self=True
)
def TEMPORARY_SAVE(kwargs):
    return kwargs


@action_interface(
    action_name="temporary-save-preview",
    component="link",
    label="Προσωρινή Αποθήκευση",
    primary=False,
    url="/vault/drafts",
    is_self=True
)
def TEMPORARY_SAVE_PREVIEW(kwargs):
    return kwargs


@action_interface(
    action_name="cancel",
    component="document-dismiss",
    label="Ακύρωση",
    primary=False,
    url="/vault",
    is_self=True,
    confirm_message="Επιβεβαιώστε την ακύρωση του εγγράφου",
    confirm_confirm_label="Επιβεβαίωση",
    confirm_cancel_label="Επιστροφή",
)
def CANCEL(kwargs):
    return kwargs


@action_interface(
    action_name="web-print",
    component="web-print",
    label="Εκτύπωση",
    primary=True,
    title="Εκτυπώστε το έγγραφο",
    icon="print"
)
def WEB_PRINT(kwargs):
    return kwargs


@action_interface(
    action_name="create",
    component="document-create",
    label="Συνέχεια",
    primary=True,
)
def CREATE(kwargs):
    return kwargs


@action_interface(
    action_name="create",
    component="document-anon-create",
    label="Συνέχεια",
    primary=True,
)
def ANON_CREATE(kwargs):
    return kwargs


@action_interface(
    action_name="new-decl",
    component="link",
    label="Νέα Αίτηση",
    icon="add",
    title="Υποβάλετε νέα αίτηση",
    helptext="Δημιουργήστε νέα αίτηση",
    primary=False,
    is_self=True,
    url=None,
)
def NEW_DECL(kwargs):
    assert kwargs["url"]
    return kwargs


@action_interface(
    action_name="revoke",
    component="document-revoke",
    label="Ανάκληση",
    title="Ανακαλέστε το έγγραφο",
    helptext="Για να σταματήσει να έχει ισχύ το έγγραφό σας, μπορείτε να κάνετε ανάκληση",
    primary=False,
    icon="settings_backup_restore",
    next_step="final_view",
)
def REVOKE(kwargs):
    return kwargs


@action_interface(
    action_name="forward",
    component="entity-forward",
    label="Προώθηση",
    primary=False,
    notify_user=True,
    message_subject="Μήνυμα-GOVGR",
    message="Λόγω αρμοδιότητας, η αίτησή σας προωθήθηκε για διεκπεραίωση σε %s",
    helptext="Επιλέξτε την θυρίδα στην οποία θέλετε να προωθήσετε το έγγραφο",
)
def FORWARD(kwargs):
    return kwargs


@action_interface(
    action_name="reply",
    component="entity-reply",
    label="Απάντηση",
    primary=True,
    reply_templates=None,
)
def REPLY(kwargs):
    assert kwargs["reply_templates"]
    return kwargs


@action_interface(
    action_name="pdf",
    component="document-download-pdf",
    label="Αποθήκευση",
    primary=True,
    title="Αποθηκεύστε στο αρχείο σας",
    helptext="Αποθηκεύστε το αρχείο PDF στη συσκευή σας.",
    icon="picture_as_pdf",
    filename="govgr_document.pdf",
)
def PDF(kwargs):
    return kwargs


@action_interface(
    action_name="pdf",
    component="document-download-pdf",
    label="Αποθήκευση",
    primary=False,
    icon="picture_as_pdf",
    filename="govgr_document.pdf",
)
def ENTITY_PDF(kwargs):
    return kwargs


ACTION_FN_MAPPING = {
    "ACTION": ACTION,
    "UPDATE": UPDATE,
    "UPDATE_FOR_REQUEST": UPDATE_FOR_REQUEST,
    "UPDATE_FOR_CONFIRMATION": UPDATE_FOR_CONFIRMATION,
    "UPDATE_FOR_SUBMISSION": UPDATE_FOR_SUBMISSION,
    "COLLECT": COLLECT,
    "ISSUE_COLLECTED": ISSUE_COLLECTED,
    "BACKSTEP": BACKSTEP,
    "SHARE": SHARE,
    "RESEND_OTP": RESEND_OTP,
    "RESEND_EMAIL_OTP": RESEND_EMAIL_OTP,
    "SMS": SMS,
    "EMAIL": EMAIL,
    "COMMUNICATION": COMMUNICATION,
    "TEMPORARY_SAVE": TEMPORARY_SAVE,
    "TEMPORARY_SAVE_PREVIEW": TEMPORARY_SAVE_PREVIEW,
    "CANCEL": CANCEL,
    "WEB_PRINT": WEB_PRINT,
    "CREATE": CREATE,
    "ANON_CREATE": ANON_CREATE,
    "NEW_DECL": NEW_DECL,
    "REVOKE": REVOKE,
    "FORWARD": FORWARD,
    "REPLY": REPLY,
    "PDF": PDF,
    "ENTITY_PDF": ENTITY_PDF,
}
