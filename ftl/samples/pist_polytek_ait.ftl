COMMON_STEP_PROPS (
    UPDATE as update;
) {
    serviceName="Αίτηση Έκδοσης Πιστοποιητικού Πολυτεκνικής Ιδιότητας";
    captionLeft="Αίτηση Έκδοσης Πιστοποιητικού Πολυτεκνικής Ιδιότητας";
} as common_step;


common_step "Στοιχεία Αιτούντος" [
    FORM "Προσωπικά Στοιχεία" [
        STRING "Όνομα" {attribute="firstname";} as firstname;
        STRING "Επώνυμο" {attribute="surname";} as surname;
        STRING "Όνομα Πατρός" {attribute="father_name";} as fathername;
        STRING "Όνομα Μητρός" {attribute="mother_name";} as mothername;
        AFM "Α.Φ.Μ." {attribute="afm";} as afm;
        DATE "Ημερομηνία Γέννησης" {attribute="birth_date"; component="three-block-date";} as birth_date;
    ] as id_verification_fs;
] edit {
    ensure_no_input=True;
    next_step="polyteknia_info";
} as id_verification;


common_step "Στοιχεία πολυτεκνικής ιδιότητας" [
    FORM [
        STRING "Αριθμός Μητρώου Α.Σ.Π.Ε." as aspe_am;
        HIERARCHICAL_SELECTOR "Σύλλογος Πολυτέκνων - Μέλος της ΑΣΠΕ" {dataset="/api/datasets/aspe_members";} as syllogos_choice;
        DATE "Λήξη τελευταίας θεώρησης ταυτότητας (βιβλιαρίου)" {component="three-block-date";} as expiration_date;
    ] as polytek_info_fs;

    FORM "Φωτογραφία πολυτεκνικής ταυτότητας" [
        STRING DISPLAY {
            value="\nΕπισυνάπτονται φωτογραφίες και των 2 όψεων της πολυτεκνικής ταυτότητας (βιβλιαρίου), \nαυτής με την τελευταία θεώρηση και αυτής με τη φωτογραφία. Και \nοι 2 όψεις είναι υποχρεωτικές. Τα τέκνα που δεν έχουν ταυτότητα επισυνάπτουν \nφωτογραφία των 2 όψεων της πολυτεκνικής ταυτότητας ενός από τους γονείς τους. \nΜέγιστο μέγεθος κάθε αρχείου 5ΜΒ.\n";
        } as photo_notes;
        ATTACHMENT OPTIONAL "Αρχείο 1ης όψης" as polit_id_photo_1;
        ATTACHMENT OPTIONAL "Αρχείο 2ης όψης" as polit_id_photo_2;
    ] as pist_polyt_photo_fs;
] edit {
    next_step="family_info";
    validator="dilosi.applications.pistopoiitiko_polyteknias.claims.common.validate_polyteknia_info_step";
} as polyteknia_info;


common_step "Στοιχεία οικογενειακής κατάστασης" [
    FORM [
        RADIO_CHOICE "Ιδιότητα" [
            parent="Γονέας";
            child="Τέκνο";
        ] as idiotita;

        INFO {
            value="Υποβάλετε πρόσφατο (να έχει εκδοθεί εντός των τελευταίων 30 ημερών πριν από την ημερομηνία της παρούσας αίτησής σας) πιστοποιητικό οικογενειακής κατάστασης με έναν από τους δύο τρόπους παρακάτω.Αν είστε τέκνο πολυτεκνικής οικογένειας, υποβάλετε το πιστοποιητικό οικογενειακής κατάστασης της πατρικής οικογένειας.";
        } as pok_note_1;

        STRING OPTIONAL "Κωδικός εγγράφου Πιστοποιητικού Οικογενειακής Κατάστασης" {
            hint="Συμπληρώστε τον κωδικό εγγράφου του Πιστοποιητικού Οικογενειακής Κατάστασης στο παρακάτω πεδίο.";
        } as pok_refcode;

        ATTACHMENT OPTIONAL "Πιστοποιητικό οικογενειακής κατάστασης" {
            filetype="pdf";
            hint="Εναλλακτικά, επισυνάψτε το Πιστοποιητικό Οικογενειακής Κατάστασης. Τα τέκνα επισυνάπτουν το Πιστοποιητικό Οικογενειακής Κατάστασης της πατρικής οικογένειας.";
        } as pok_file;

        INFO {
            value="Σε περίπτωση που δεν έχετε εκδώσει το σχετικό πιστοποιητικό, παρακαλούμε μεταβείτε στην Ψηφιακή Υπηρεσία Έκδοσης η οποία βρίσκεται <a href='https://www.gov.gr/ipiresies/oikogeneia/oikogeneiake-katastase/pistopoietiko-oikogeneiakes-katastases' target='_blank'>εδώ</a>.";
        } as pok_note_2;

        CHOICE "Το πιστοποιητικό προορίζεται για χρήση:" [
            ΓιατοΑΣΕΠ="Για το ΑΣΕΠ";
            ΓιαΠρόσληψη="Για Πρόσληψη";
            ΓιαΔιαγωνισμό="Για Διαγωνισμό";
            ΓιαΜετεγγραφήσεάλληΣχολή="Για Μετεγγραφή σε άλλη Σχολή";
            ΓιαΣτρατιωτικέςΣχολέςκαιΣχολέςΣωμάτων="Για Στρατιωτικές Σχολές και Σχολές Σωμάτων";
            ΓιατηΣτρατιωτικήθητεία="Για τη Στρατιωτική θητεία";
            ΓιαΛοιπά="Για Λοιπά";
        ] as pist_use;

        STRING OPTIONAL "Λοιπά" {
            hint="Συμπληρώστε τη χρήση για την οποία προορίζεται το πιστοποιητικό αν επιλέξατε \"Για Λοιπά\"";
        } as other_use;

        TEXT OPTIONAL "Παρατηρήσεις" as comments;
    ] as family_info_fs;
] edit {
    next_step="contact_info";
    validator="dilosi.applications.pistopoiitiko_polyteknias.claims.common.check_family_info_fs_fields";
} as family_info;


common_step "Στοιχεία Επικοινωνίας" [
    FORM [
        EMAIL "Διεύθυνση Ηλεκτρονικού Ταχυδρομείου" as email;
        MOBILE "Κινητό Τηλέφωνο" as mobile;
    ] as contact_info_fs;
] edit {
    next_step="preview";
} as contact_info;


common_step "Προεπισκόπηση" (
    UPDATE_FOR_SUBMISSION as submit;
) [
    VIEW id_verification_fs;

    VIEW "Στοιχεία Πολυτεκνικής Ιδιότητας" [
        aspe_am;
        syllogos_choice;
        expiration_date;
        polit_id_photo_1;
        polit_id_photo_2;
    ] {
        omit_empty_values=True;
    } as polytek_info_fs;

    VIEW "Στοιχεία Οικογενειακής Κατάστασης" [
        idiotita;
        pok_file;
        pok_refcode;
        STRING DISPLAY "Σύνδεσμος Πιστοποιητικού Οικογενειακής Κατάστασης" {
            sources="field:pok_refcode";
            value_constructor="dilosi.applications.pistopoiitiko_polyteknias.claims.common.construct_pok_validation_url";
            safe=True;
        } as pok_validation_url;
        pist_use;
        other_use;
        comments;
    ] {
        omit_empty_values=True;
    } as family_info_fs;

    VIEW contact_info_fs;

] edit {
    ensure_no_input=True;
    next_step="final_view";
} as preview;


PDF_SPEC [
    HEADER as header;
    DOC_TITLE [
        TITLE {value="Αίτηση Έκδοσης Πιστοποιητικού Πολυτεκνικής Ιδιότητας";} as title;
    ] as doc_title;
    TABLE case_id_fs {
        component="one-liner-table";
    };
    TABLE id_verification_fs;
    TABLE polytek_info_fs;
    TABLE family_info_fs;
    TABLE contact_info_fs;
    SIGNATURE as signature;
] as pdf_spec;


common_step "Τελική Προβολή" (
    PDF(pdf_spec;);
) [
    VIEW [
        STRING "Αρ. Υπόθεσης" {sources="declaration:case";} as case_id;
    ] as case_id_fs;
    VIEW id_verification_fs;
    VIEW polytek_info_fs;
    VIEW family_info_fs;
    VIEW contact_info_fs;
] edit {
    - next_step;
    is_final_view=True;
} as final_view;


TEMPLATE {
    refname="PIST-POLYTEK-AIT-DEMO";
    caption="Αίτηση Έκδοσης Πιστοποιητικού Πολυτεκνικής Ιδιότητας";
    owner="ASPE";
    is_official=True;
    requires_case=True;
    exempted_claims=["mobile_certified_login","is_citizen_user"];
};
