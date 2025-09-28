info_msg_value = "Οι τιμές των πεδίων της σελίδας έχουν ανακτηθεί από το Φορολογικό Μητρώο και το Εθνικό Μητρώο Επικοινωνίας (ΕΜΕπ). Στην υπηρεσία Βεβαίωση φορολογικού μητρώου μπορείτε να δείτε τα στοιχεία σας στο Φορολογικό Μητρώο, ενώ στην υπηρεσία Εθνικό Μητρώο Επικοινωνίας (ΕΜΕπ) μπορείτε να δείτε και να τροποποιήσετε τα στοιχεία επικοινωνίας σας.";
introduction_value = "Με ατομική μου ευθύνη και γνωρίζοντας τις κυρώσεις<sup>(2)</sup>, που προβλέπονται από τις διατάξεις της παρ. 6 του άρθρου 22 του Ν. 1599/1986, δηλώνω ότι:";
recipient_help_text_value = "Συμπληρώστε το όνομα του αποδέκτη προς τον οποίο θέλετε να γνωστοποιήσετε το έγγραφο για να ολοκληρώσετε τη διαδικασία.";
warning_value = "Η ακρίβεια των στοιχείων που υποβάλλονται με αυτή τη δήλωση μπορεί να ελεγχθεί με βάση το αρχείο άλλων υπηρεσιών (άρθρο 8 παρ. 4 Ν. 1599/1986).";
footnote1_value = "(1) Αναγράφεται από τον ενδιαφερόμενο πολίτη η αρχή ή η υπηρεσία του δημόσιου τομέα όπου απευθύνεται η αίτηση.";
footnote2_value = "(2) Γνωρίζω ότι: Όποιος εν γνώσει του δηλώνει ψευδή γεγονότα ή αρνείται ή αποκρύπτει τα αληθινά με έγγραφη υπεύθυνη δήλωση του άρθρου 8 τιμωρείται με φυλάκιση τουλάχιστον τριών μηνών. Εάν ο υπαίτιος αυτών των πράξεων σκόπευε να προσπορίσει στον εαυτόν του ή σε άλλον περιουσιακό όφελος βλάπτοντας τρίτον ή σκόπευε να βλάψει άλλον, τιμωρείται με κάθειρξη μέχρι 10 ετών.";


STEP "Στοιχεία Δηλούντος" (
    UPDATE as update;
) [
    VIEW "Μήνυμα Πληροφόρησης" [
        INFO {
            value=info_msg_value;
        } as info_msg;
    ] as info_msg_fs;

    FORM "Προσωπικά Στοιχεία" [
        STRING "Όνομα" as solemn_firstname;
        STRING "Επώνυμο" as solemn_surname;
        STRING "Όνομα Πατρός" as solemn_father_fullname;
        STRING "Όνομα Μητρός" as solemn_mother_fullname;
        DATE "Ημερομηνία Γέννησης" {
            labels__day="01";
            labels__month="01";
            labels__year="2000";
        } as solemn_birth_date;
        STRING "Τόπος Γέννησης" as solemn_birth_place;
        STRING "Αριθμός Δελτίου Ταυτότητας" as solemn_adt;
        AFM as solemn_afm;
    ] as personal;

    FORM "Διεύθυνση Κατοικίας" [
        STRING "Τόπος Κατοικίας" as solemn_residence;
        STRING "Οδός" as solemn_street;
        STRING "Αριθμός" as solemn_street_number;
        STRING "Τ.Κ." as solemn_tk;
    ] as address;

    FORM "Στοιχεία Επικοινωνίας" [
        PHONE "Τηλέφωνο" as solemn_tel;
        EMAIL "Δ/νση Ηλεκτρ. Ταχυδρομείου (E-mail)" as solemn_email;
    ] as contact;
] {
    next_step="body";
    captionLeft="Υπεύθυνη Δήλωση";
} as personal;


STEP "Συμπληρώστε το κείμενο της δήλωσης" (
    update;
) [
    FORM [
        STRING DISPLAY {
            value=introduction_value;
        } as introduction;
        TEXT {
            format="plaintext";
        } as free_text;
    ] as body;
] {
    next_step="recipient";
    captionLeft="Υπεύθυνη Δήλωση";
} as body;


STEP "Ποια είναι τα στοιχεία του αποδέκτη του εγγράφου σας" (
    update;
) [
    FORM [
        STRING DISPLAY {
            value=recipient_help_text_value;
        } as recipient_help_text;
        RECIPIENT "Προς" as solemn_recipient;
    ] as recipient;
] {
    next_step="preview";
    captionLeft="Υπεύθυνη Δήλωση";
} as recipient;


STEP "Προεπισκόπηση Δήλωσης" (
    update;
) [
    VIEW [
        STRING {
            value=warning_value;
        } as warning;
    ] as preamble;

    VIEW "Αποδέκτης<sup>(1)</sup>" [
        solemn_recipient;
    ] as recipient;

    VIEW "Κείμενο Δήλωσης" [
        introduction;
        free_text;
    ] as body;

    VIEW "Στοιχεία Δηλούντος" [
        solemn_firstname;
        solemn_surname;
        solemn_father_fullname;
        solemn_mother_fullname;
        solemn_birth_date;
        solemn_birth_place;
        solemn_adt;
        solemn_tel;
        solemn_residence;
        solemn_street;
        solemn_street_number;
        solemn_tk;
        solemn_afm;
        solemn_email;
    ] as personal_all;

    VIEW "Υποσημειώσεις" [
        STRING {
            value=footnote1_value;
        } as footnote1;
        STRING {
            value=footnote2_value;
        } as footnote2;
    ] as footnotes;
] {
    ensure_no_input=True;
    captionLeft="Υπεύθυνη Δήλωση";
    next_step="otp";
} as preview;


OTP "Εισαγωγή κωδικού επιβεβαίωσης" {
    next_step="final_view";
} as otp;


preview "Προβολή" (
    PDF(
        PDF_SPEC [
            HEADER as header;
            preamble;
            recipient;
            body;
            personal_all;
            FOOTNOTES footnotes;
        ] as pdf_spec;
    );
) edit {
    - next_step;
} as final_view;


TEMPLATE {
    refname="TEST";
    shortname="TEST";
    owner="System";
    description="TEST";
    is_official=False;
    requires_case=True;
};
