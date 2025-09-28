from ftl.internal.interface import (
    FIELDSET as fieldset_shell, get_obj_interface
)
from ftl.internal.standardized_fields import (
    PDF_IMAGE, QRCODE, REFCODE, FIELD, DATE, STRING
)

fieldset_interface = get_obj_interface(fieldset_shell)


@fieldset_interface()
def FIELDSET(kwargs):
    return kwargs


@fieldset_interface(component="form")
def FORM(kwargs):
    return kwargs


@fieldset_interface(component="values-list")
def VIEW(kwargs):
    return kwargs


@fieldset_interface(component="table")
def TABLE(kwargs):
    return kwargs


@fieldset_interface(component="footnotes")
def FOOTNOTES(kwargs):
    return kwargs


@fieldset_interface(
    component="header",
    fields=[
        PDF_IMAGE(
            field_name="emblem",
            coordinates=(7.5, 26.4, 6, 2.581),
            value="hellenic_coat_of_arms_el_pdf",
        ),
        QRCODE(),
        REFCODE(),
    ],
)
def HEADER(kwargs):
    return kwargs


@fieldset_interface(
    component="one-liner-table",
    spaceAfter=30,
)
def DOC_TITLE(kwargs):
    return kwargs


@fieldset_interface(
    component="signature",
    fields=[
        DATE(
            field_name="sign_date",
            user_input_mode="noinput",
            sources="declaration:timestamp",
            value_constructor="dilosi.interop_logic.common.get_local_date",
            is_display_field=True,
        ),
        STRING(
            field_name="signer_title",
            user_input_mode="noinput",
            value="Ο - Η Αιτ.",
            is_display_field=True,
        ),
        STRING(
            field_name="signer_empty",
            user_input_mode="noinput",
            value="",
            is_display_field=True,
        ),
        FIELD(
            field_name="signer_name",
            user_input_mode="noinput",
            value="{firstname} {surname}",
            component="dynamically-filled-text",
            is_display_field=True,
            emph=False,
        ),
    ],
    spaceBefore=20,
)
def SIGNATURE(kwargs):
    return kwargs


FIELDSET_FN_MAPPING = {
    "FIELDSET": FIELDSET,
    "FORM": FORM,
    "VIEW": VIEW,
    "TABLE": TABLE,
    "FOOTNOTES": FOOTNOTES,
    "HEADER": HEADER,
    "DOC_TITLE": DOC_TITLE,
    "SIGNATURE": SIGNATURE,
}
