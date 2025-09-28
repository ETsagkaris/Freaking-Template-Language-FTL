COMMON_STEP_PROPS (
    UPDATE as update;
) {
    serviceName="Βεβαίωση Φοίτησης";
    captionLeft="Βεβαίωση Φοίτησης";
} as common_step;


common_step "Προσωπικά Στοιχεία" [
    FORM "Προσωπικά Στοιχεία" [
        STRING NOINPUT "Όνομα" {
            attribute="firstname";
            enforceUppercase=True;
        } as firstname;
        STRING NOINPUT "Επώνυμο" {
            attribute="surname";
            enforceUppercase=True;
        } as surname;
        STRING NOINPUT "Όνομα Πατέρα" {
            attribute="father_name";
            enforceUppercase=True;
        } as father_name;
        STRING NOINPUT "Όνομα Μητρός" {
            attribute="mother_name";
            enforceUppercase=True;
        } as mother_name;
        DATE NOINPUT "Ημερομηνία Γέννησης" {
            attribute="birth_date";
        } as birth_date;
        AFM NOINPUT "Α.Φ.Μ." {
            attribute="afm";
        } as afm;
    ] as personal;
] edit {
    next_step="self_or_child";
} as personal_info;


common_step "Επιλέξτε για ποιον θέλετε να εκδώσετε την Βεβαίωση Φοίτησης" [
    FORM [
        RADIO_CHOICE "Επιλογή" [
            self="Για εμένα";
            child="Για το παιδί μου";
        ] as option;
    ] as option_fs;
] edit {
    decide_next_step="dilosi.interop_logic.common.get_self_or_child_next_step";
    possible_next_steps=["more_personal_info", "choose_child"];
} as self_or_child;


common_step "Στοιχεία Μαθητή" [
    FORM "Στοιχεία Μαθητή" [
        STRING NOINPUT "Όνομα" {attribute="student_first_second_name:firstname";} as input_firstname;
        STRING NOINPUT "Επώνυμο" {attribute="surname";} as input_surname;
        STRING NOINPUT "Όνομα Πατρός" {attribute="father_name";} as input_father_name;
        STRING NOINPUT "Όνομα Μητρός" {attribute="mother_name";} as input_mother_name;
        DATE NOINPUT "Ημερομηνία γέννησης" {
            attribute="birth_date";
            component="three-block-date";
        } as input_birth_date;
        RADIO_CHOICE "Φύλο" [
            Α="Άρρεν";
            Θ="Θήλυ";
        ] as input_gender;
    ] as student_input;
] edit {
    next_step="preview";
} as more_personal_info;


common_step "Επιλέξτε παιδί" [

    FORM [
        STRING NOINPUT {
            attribute="children_list";
            component="hidden";
        } as children;
        RADIO_CHOICE "Επιλέξτε" {
            choices_source_fn="dilosi.interop_logic.common.get_child_choices";
        } as child_choice;
    ] as choose_child_fs;
] edit {
    next_step="child_info";
} as choose_child;


common_step "Στοιχεία Μαθητή" [
    student_input edit [
        input_firstname edit {attribute="student_first_second_name:firstname";};
        input_surname edit {attribute="child_choice_info:lastname";};
        input_father_name edit {attribute="child_choice_info:fathername";};
        input_mother_name edit {attribute="child_choice_info:mothername";};
        input_birth_date edit {attribute="child_choice_info:birthdate";};
    ];
] edit {
    next_step="preview";
} as child_info;


common_step "Προεπισκόπηση" (
  UPDATE_FOR_SUBMISSION as submit;
) [
    VIEW "Στοιχεία Μαθητή" [
        STRING "Όνομα" {attribute="vevaiosi_foitisis:firstName";} as student_firstName;
        STRING "Επώνυμο" {attribute="vevaiosi_foitisis:lastName";} as student_lastName;
        STRING "Πατρώνυμο" {attribute="vevaiosi_foitisis:fatherFirstName";} as student_fatherFirstName;
        STRING "Μητρώνυμο" {attribute="vevaiosi_foitisis:motherFirstname";} as student_motherFirstname;
    ] as student_info;
    
    VIEW "Στοιχεία Σχολείου" [
        STRING "Όνομα Σχολείου Φοίτησης" {attribute="vevaiosi_foitisis:unitName";} as school_unitName;
        STRING "Σχολικό έτος" {attribute="vevaiosi_foitisis:didacticYear";} as school_didacticYear;
        STRING "Τάξη Εγγραφής στο τρέχον σχολικό έτος" {attribute="vevaiosi_foitisis:levelName";} as school_levelName;
        STRING "Αριθμός Μητρώου (ΑΜ) του μαθητή στο σχολείο" {attribute="vevaiosi_foitisis:registrationNumber";} as student_AM;
        STRING "Περιφερειακή  Διεύθυνση Εκπαίδευσης όπου υπάγεται το σχολείο" {attribute="vevaiosi_foitisis:precinctName";} as school_precinctName;
        STRING "Διεύθυνση Εκπαίδευσης όπου υπάγεται το σχολείο" {attribute="vevaiosi_foitisis:divisionName";} as school_divisionName;
        STRING "Ταχ. Δ/νση Σχολείου" {attribute="vevaiosi_foitisis:unitAddress";} as school_unitAddress;
        STRING "Τηλέφωνο Σχολείου" {attribute="vevaiosi_foitisis:unitTelephone";} as school_unitTelephone;
        STRING "E-mail Σχολείου" {attribute="vevaiosi_foitisis:unitEmail";} as school_unitEmail;
    ] as school_info;
] edit {
    next_step="final_view";
    ensure_no_input=True;
} as preview;


preview "Τελική Προβολή" (
    PDF(
        PDF_SPEC [
            HEADER as header;
            TABLE [
                STRING {
                    format="plaintext";
                    value="Υπουργείο Παιδείας, Θρησκευμάτων και Αθλητισμού\nΓενική Γραμματεία Πρωτοβάθμιας,\nΔευτεροβάθμιας Εκπαίδευσης και Ειδικής Αγωγής\nΓενική Διεύθυνση Σπουδών Πρωτοβάθμιας και\nΔευτεροβάθμιας Εκπαίδευσης";
                } as ypourgeio;
            ] {
                component="one-liner-table";
            } as ypourgeio_fs;

            DOC_TITLE [
                TITLE {value="ΒΕΒΑΙΩΣΗ ΦΟΙΤΗΣΗΣ";} as title;
            ] as doc_title;

            TABLE [
                STRING {value="Βεβαιώνεται ότι ο/η μαθητής/τρια:";} as before_student;
            ] {
                component="one-liner-table";
            } as before_student_fs;

            TABLE student_info edit [
                firstname edit {component="hidden";};
                surname edit {component="hidden";};
            ] edit {
                - title;
                auto_columns=2;
            };

            TABLE [
                STRING {
                    sources="field:school_didacticYear";
                    value_constructor="dilosi.applications.vevaiosi_foitisis.claims.common.text_with_current_school_year";
                } as before_school;
            ] {
                component="one-liner-table";
            } as before_school_fs;

            TABLE school_info edit {
                - title;
                auto_columns=2;
            };

            TABLE [
                STRING {
                    value="Η Βεβαίωση αυτή χορηγείται προκειμένου να χρησιμοποιηθεί για κάθε νόμιμη χρήση.";
                } as before_signature;
            ] {
                component="one-liner-table";
            } as before_signature_fs;
            SIGNATURE as signature;
        ] as pdf_spec;
    );
) edit {
    - next_step;
} as final_view;


TEMPLATE {
    refname="VEVAIOSI-FOITISIS-DEMO";
    caption="Βεβαίωση Φοίτησης";
    owner="System";
    is_official=True;
    requires_case=True;
    extra_required_claims=["mobile_certified_login"];
};
