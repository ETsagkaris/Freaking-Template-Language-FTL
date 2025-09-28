from ftl.internal.interface import (
    FIELD as field_shell, get_obj_interface
)

field_interface = get_obj_interface(field_shell)


@field_interface()
def FIELD(kwargs):
    return kwargs


@field_interface(component="string", datatype="string")
def STRING(kwargs):
    return kwargs


@field_interface(component="text", datatype="text")
def TEXT(kwargs):
    return kwargs


@field_interface(component="int", datatype="int")
def INT(kwargs):
    return kwargs


@field_interface(component="recipient", datatype="recipient")
def RECIPIENT(kwargs):
    return kwargs


@field_interface(
    field_name="postal_code",
    component="postal_code",
    datatype="postal_code",
)
def POSTAL_CODE(kwargs):
    return kwargs


@field_interface(
    field_name="afm",
    title="ΑΦΜ",
    component="afm",
    datatype="afm",
)
def AFM(kwargs):
    return kwargs


@field_interface(
    field_name="amka",
    title="ΑΜΚΑ",
    component="amka",
    datatype="amka",
)
def AMKA(kwargs):
    return kwargs


@field_interface(
    field_name="landline_phone",
    title="Σταθερό Τηλέφωνο",
    component="landline_phone",
    datatype="landline_phone",
)
def LANDLINE(kwargs):
    return kwargs


@field_interface(
    field_name="mobile_phone",
    title="Κινητό Τηλέφωνο",
    component="mobile_phone",
    datatype="mobile_phone",
)
def MOBILE(kwargs):
    return kwargs


@field_interface(
    field_name="phone",
    title="Τηλέφωνο",
    component="phone",
    datatype="phone",
)
def PHONE(kwargs):
    return kwargs


@field_interface(
    field_name="email",
    title="Email",
    component="email",
    datatype="email",
)
def EMAIL(kwargs):
    return kwargs


@field_interface(
    field_name="iban",
    component="iban",
    datatype="iban",
    country="gr",
)
def IBAN(kwargs):
    return kwargs


@field_interface(
    field_name="attachment",
    title="Συνημμένο έγγραφο",
    component="attachment",
    datatype="attachment",
    file_max_size=None,  # usually 10 * 2 ** 20
)
def ATTACHMENT(kwargs):
    return kwargs


@field_interface(
    field_name="attachment",
    title="Συνημμένο έγγραφο",
    component="attachment",
    datatype="attachment",
    filetype="pdf",
    file_max_size=None,  # usually 10 * 2 ** 20
)
def PDF(kwargs):
    return kwargs


@field_interface(
    field_name="attachment",
    title="Συνημμένο έγγραφο",
    component="attachment",
    datatype="attachment",
    filetype="pdf-for-mark",
    file_max_size=None,  # usually 10 * 2 ** 20
)
def PDF_FOR_MARK(kwargs):
    return kwargs


@field_interface(
    component="choice",
    datatype="choice",
    choices=None,
    choices_source_fn=None,
)
def CHOICE(kwargs):
    assert kwargs["choices"] or kwargs["choices_source_fn"]
    return kwargs


@field_interface(
    component="radio-choice",
    datatype="radio-choice",
    choices=None,
    choices_source_fn=None,
)
def RADIO_CHOICE(kwargs):
    assert kwargs["choices"] or kwargs["choices_source_fn"]
    return kwargs


@field_interface(
    component="multiple-choice",
    datatype="multiple-choice",
    choices=None,
    choices_source_fn=None,
)
def MULTIPLE_CHOICE(kwargs):
    assert kwargs["choices"] or kwargs["choices_source_fn"]
    return kwargs


@field_interface(
    component="preference-multiple-choice",
    datatype="preference-multiple-choice",
    choices=None,
    choices_source_fn=None,
)
def PREFERENCE_MULTIPLE_CHOICE(kwargs):
    assert kwargs["choices"] or kwargs["choices_source_fn"]
    return kwargs


@field_interface(
    component="multiple-choice",
    datatype="multiple-choice",
    checkbox_key="ΝΑΙ",
    checkbox_value=None,
)
def CHECKBOX(kwargs):
    checkbox_key = kwargs.pop('checkbox_key')
    checkbox_value = kwargs.pop('checkbox_value')
    assert checkbox_key and checkbox_value
    kwargs["choices"] = [(checkbox_key, checkbox_value)]
    return kwargs


@field_interface(
    component="hierarchical-selector",
    dataset=None,
    dataset_source_fn=None,
    dataset_filter_field=None,
    initial_loading_levels=None,
)
def HIERARCHICAL_SELECTOR(kwargs):
    assert kwargs["dataset"] or kwargs["dataset_source_fn"]
    return kwargs


@field_interface(
    field_name="refcode",
    component="refcode",
    sources="declaration:reference_code",
    value_constructor="dilosi.interop_logic.common.from_singleton_list",
    later_pages=True,
    is_display_field=True,
    label=None,  # default in pdf mechanism is 'Κωδικός'
)
def REFCODE(kwargs):
    return kwargs


@field_interface(
    field_name="date",
    component="date",
    datatype="date",
    min=None,
    max=None,
    labels__day=None,
    labels__month=None,
    labels__year=None,
)
def DATE(kwargs):
    return kwargs


@field_interface(
    field_name="date",
    component="three-block-date",
    datatype="date",
    min=None,
    max=None,
    labels__day=None,
    labels__month=None,
    labels__year=None,
)
def DATE_3B(kwargs):
    return kwargs


@field_interface(
    field_name="date",
    component="five-block-date",
    datatype="five-block-date",
    min=None,
    max=None,
    labels__day=None,
    labels__month=None,
    labels__year=None,
)
def DATE_5B(kwargs):
    return kwargs


@field_interface(
    field_name="rate",
    component="rate",
    datatype="rate",
    dependencies=None,
    dependencies_error_message=None,
)
def RATE(kwargs):
    return kwargs


@field_interface(
    field_name="info_msg",
    component="quote",
    mode="info",
    user_input_mode="display",
)
def INFO(kwargs):
    return kwargs


@field_interface(
    field_name="warning_msg",
    component="quote",
    mode="warning",
    user_input_mode="display",
)
def WARNING(kwargs):
    return kwargs


@field_interface(
    field_name="error_msg",
    component="quote",
    mode="error",
    user_input_mode="display",
)
def ERROR(kwargs):
    return kwargs


@field_interface(
    field_name="url_param",
    component="url-param",
    param_name=None,
)
def URL_PARAM(kwargs):
    assert kwargs["param-name"]
    return kwargs


@field_interface(
    field_name="consent_content",
    component="consent-content",
    display_values=None,
    data_label=None,
    transaction_label=None,
    recipient_label=None,
)
def CONSENT_CONTENT(kwargs):
    assert kwargs["display_values"]
    return kwargs


@field_interface(
    component="image",
    datatype="attachment",
    user_input_mode="display",
)
def IMAGE(kwargs):
    return kwargs


@field_interface(
    component="pdf-image",
    user_input_mode="display",
)
def PDF_IMAGE(kwargs):
    return kwargs


@field_interface(
    field_name="qrcode",
    component="qrcode",
    user_input_mode="noinput",
    sources="declaration:reference_code declaration:validation_context",
    value_constructor="dilosi.interop_logic.common.create_document_uri",
    is_display_field=True,
)
def QRCODE(kwargs):
    return kwargs


@field_interface(
    field_name="sign_date",
    component="date",
    user_input_mode="noinput",
    sources="declaration:timestamp",
    value_constructor="dilosi.interop_logic.common.get_local_date",
    is_display_field=True,
)
def SIGN_DATE(kwargs):
    return kwargs


@field_interface(
    field_name="signer_title",
    component="string",
    user_input_mode="noinput",
    value="Ο - Η Αιτ.",
    is_display_field=True,
)
def SIGNER_TITLE(kwargs):
    return kwargs


@field_interface(
    field_name="signer_empty",
    component="string",
    user_input_mode="noinput",
    value="",
    is_display_field=True,
)
def SIGNER_EMPTY(kwargs):
    return kwargs


@field_interface(
    field_name="signer_name",
    component="dynamically-filled-text",
    user_input_mode="noinput",
    value="{firstname} {surname}",
    is_display_field=True,
    emph=False,
)
def SIGNER_NAME(kwargs):
    return kwargs


@field_interface(
    field_name="title",
    component="doc_title",
    user_input_mode="noinput",
)
def TITLE(kwargs):
    return kwargs


@field_interface(
    field_name="subtitle",
    component="doc_subtitle",
    user_input_mode="noinput",
)
def SUBTITLE(kwargs):
    return kwargs


FIELD_FN_MAPPING = {
    "FIELD": FIELD,
    "STRING": STRING,
    "TEXT": TEXT,
    "INT": INT,
    "RECIPIENT": RECIPIENT,
    "POSTAL_CODE": POSTAL_CODE,
    "AFM": AFM,
    "AMKA": AMKA,
    "LANDLINE": LANDLINE,
    "MOBILE": MOBILE,
    "PHONE": PHONE,
    "EMAIL": EMAIL,
    "IBAN": IBAN,
    "ATTACHMENT": ATTACHMENT,
    "PDF": PDF,
    "PDF_FOR_MARK": PDF_FOR_MARK,
    "CHOICE": CHOICE,
    "RADIO_CHOICE": RADIO_CHOICE,
    "MULTIPLE_CHOICE": MULTIPLE_CHOICE,
    "PREFERENCE_MULTIPLE_CHOICE": PREFERENCE_MULTIPLE_CHOICE,
    "CHECKBOX": CHECKBOX,
    "HIERARCHICAL_SELECTOR": HIERARCHICAL_SELECTOR,
    "REFCODE": REFCODE,
    "DATE": DATE,
    "DATE_3B": DATE_3B,
    "DATE_5B": DATE_5B,
    "RATE": RATE,
    "INFO": INFO,
    "WARNING": WARNING,
    "ERROR": ERROR,
    "URL_PARAM": URL_PARAM,
    "CONSENT_CONTENT": CONSENT_CONTENT,
    "IMAGE": IMAGE,
    "PDF_IMAGE": PDF_IMAGE,
    "QRCODE": QRCODE,
    "TITLE": TITLE,
    "SUBTITLE": SUBTITLE,
    "SIGN_DATE": SIGN_DATE,
    "SIGNER_TITLE": SIGNER_TITLE,
    "SIGNER_EMPTY": SIGNER_EMPTY,
    "SIGNER_NAME": SIGNER_NAME,
}
