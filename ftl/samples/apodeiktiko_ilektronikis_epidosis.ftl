COMMON_STEP_PROPS (
    UPDATE as update;
) {
    serviceName="Αποδεικτικό έγγραφο ηλεκτρονικής επίδοσης";
    captionLeft="Αποδεικτικό έγγραφο ηλεκτρονικής επίδοσης";
} as common_step;


common_step "Κωδικός εγγράφου (που έχει επιδοθεί από τη θυρίδα ή το Π.Σ. του Δήμου)" [
    FORM [
        STRING "Κωδικός εγγράφου" as epidosi_ref_code;
    ] as epidosi_input_fs;
] edit {
    next_step="view_epidosi";
    validator="dilosi.applications.epidosi_eggrafou.claims.apodeiktiko_ilektronikis_epidosis_fields.validate_application";
} as epidosi_input;


common_step "Στοιχεία επίδοσης" [
    VIEW [
        STRING "Αποστολέας" {attribute="apodeiktiko_ilektronikis_epidosis_fields:sender";} as sender;
    ] as sender_fs;

    VIEW "Υπόχρεο φυσικό πρόσωπο" [
        AFM "ΑΦΜ" {attribute="apodeiktiko_ilektronikis_epidosis_fields:afm";} as afm;
        STRING "Όνομα" {attribute="apodeiktiko_ilektronikis_epidosis_fields:firstname";} as firstname;
        STRING "Επώνυμο" {attribute="apodeiktiko_ilektronikis_epidosis_fields:lastname";} as lastname;
    ] as citizen_info_fs;

    VIEW "Ηλεκτρονική επίδοση" [
        STRING "Τίτλος επίδοσης" {attribute="apodeiktiko_ilektronikis_epidosis_fields:application_title";} as application_title;
        STRING "Κωδικός εγγράφου που επιδόθηκε" {attribute="apodeiktiko_ilektronikis_epidosis_fields:application_refcode";} as application_refcode;
        STRING "Ημερομηνία ανάρτησης" {attribute="apodeiktiko_ilektronikis_epidosis_fields:upload_date";} as upload_date;
        STRING "Ημερομηνία ανάγνωσης από τον πολίτη" {attribute="apodeiktiko_ilektronikis_epidosis_fields:retrieved_date";} as retrieved_date;
        STRING "Κατάσταση ανάγνωσης" {attribute="apodeiktiko_ilektronikis_epidosis_fields:retrieval_status";} as retrieval_status;
        STRING "Παρατηρήσεις" {attribute="apodeiktiko_ilektronikis_epidosis_fields:notes";} as notes;
    ] as application_fs;
] edit {
    ensure_no_input=True;
    next_step="preview";
} as view_epidosi;


view_epidosi "Προεπισκόπηση" (
    UPDATE_FOR_SUBMISSION as submit;
) edit {
    ensure_no_input=True;
    next_step="final_view";
} as preview;


preview "Προβολή" (
    PDF(
        PDF_SPEC [
            HEADER as header;
            DOC_TITLE [
                TITLE {value="Αποδεικτικό έγγραφο ηλεκτρονικής επίδοσης";} as title;
                SUBTITLE {attribute="apodeiktiko_ilektronikis_epidosis_fields:issue_date";} as issue_date;
                SUBTITLE {value="Βεβαιώνεται ότι πραγματοποιήθηκε η ηλεκτρονική επίδοση με τα εξής στοιχεία:";} as subtitle;
            ] as doc_title;
            TABLE sender_fs;
            TABLE citizen_info_fs;
            TABLE application_fs;
        ] as pdf_spec;
    );
) edit {
    - next_step;
} as final_view;


TEMPLATE {
    refname="APODEIKTIKO-ILEKTRONIKIS-EPIDOSIS-DEMO";
    caption="Αποδεικτικό έγγραφο ηλεκτρονικής επίδοσης";
    owner="ΔΗΜΟΣ-ΕΠΙΔΟΣΕΙΣ";
    is_official=True;
    action_on_issue="dilosi.interop_logic.common.create_finished_entity_inbox";
    extra_required_claims=["is_admin|is_service"];
    exempted_claims=["mobile_certified_login","is_citizen_user","govgr_login"];
};