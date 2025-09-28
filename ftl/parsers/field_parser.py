from ftl.internal.standardized_fields import (
    FIELD_FN_MAPPING
)
from ftl.parsers.config_parser import parse_config
from ftl.parsers.utils import (
    parse_objs,
    decide_from_ref_and_orig
)


def maybe_is_reference(context, field):
    orig_field = field
    update_context = True

    if str(field).startswith('<FieldReference'):
        orig_field = context["fields"][field.name]
        if not field.alias:
            update_context = False

    field.name = getattr(field, "alias", field.name) or orig_field.name
    field.title = field.title or getattr(orig_field, "title", None)
    field.datatype = field.datatype or getattr(orig_field, "datatype", None)
    field.input_mode = field.input_mode or getattr(
        orig_field, "input_mode", None
    )
    field.choices = getattr(field, "choices", []) or getattr(
        orig_field, "choices", []
    )
    field.config = decide_from_ref_and_orig(field, orig_field, "config")

    return field, update_context


def parse_field(context, field, display_mode="default"):
    kwargs = {}

    field, update_context = maybe_is_reference(context, field)

    kwargs["field_name"] = field.name

    if field.title:
        kwargs["title"] = field.title
    if field.input_mode:
        kwargs["user_input_mode"] = field.input_mode.lower()

    parse_config(kwargs, context, field.config)

    if field.choices:
        kwargs["choices"] = []
        for choice in field.choices:
            kwargs["choices"].append((choice.key, choice.value))

    if update_context and display_mode != "pdf":
        context["fields"][field.name] = field

    field_fn = FIELD_FN_MAPPING[field.datatype]
    field_spec = field_fn(
        **kwargs,
        display_mode=display_mode,
    )

    return field.name, field_spec


def parse_fields(kwargs, context, fields, display_mode="default"):
    field_specs = {}
    parse_objs(
        field_specs, context, fields, parse_field, display_mode=display_mode
    )
    kwargs["fields"] = list(field_specs.values()) if field_specs else []
