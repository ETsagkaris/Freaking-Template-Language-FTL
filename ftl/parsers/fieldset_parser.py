from ftl.internal.standardized_fieldsets import (
    FIELDSET_FN_MAPPING
)
from ftl.parsers.field_parser import parse_fields
from ftl.parsers.config_parser import parse_config
from ftl.parsers.utils import (
    parse_objs,
    decide_from_ref_and_orig
)


def maybe_is_reference(context, fieldset):
    orig_fieldset = fieldset
    update_context = True

    if str(fieldset).startswith('<FieldsetReference'):
        orig_fieldset = context["fieldsets"][fieldset.name]
        if not fieldset.alias:
            update_context = False

    fieldset.name = getattr(
        fieldset, "alias", fieldset.name
    ) or orig_fieldset.name
    fieldset.title = fieldset.title or getattr(orig_fieldset, "title", None)
    fieldset.component = fieldset.component or getattr(
        orig_fieldset, "component", None
    )
    fieldset.fields = decide_from_ref_and_orig(
        fieldset, orig_fieldset, "fields"
    )
    fieldset.config = decide_from_ref_and_orig(
        fieldset, orig_fieldset, "config"
    )

    return fieldset, update_context


def parse_fieldset(context, fieldset, display_mode="default"):
    kwargs = {}

    fieldset, update_context = maybe_is_reference(context, fieldset)

    kwargs["fieldset_name"] = f"pdf_{fieldset.name}" if display_mode == "pdf" \
        else fieldset.name

    if fieldset.title:
        kwargs["title"] = fieldset.title

    parse_config(kwargs, context, fieldset.config)
    if fieldset.fields:
        parse_fields(
            kwargs, context, fieldset.fields, display_mode=display_mode
        )

    if update_context and display_mode != "pdf":
        context["fieldsets"][fieldset.name] = fieldset

    fieldset_fn = FIELDSET_FN_MAPPING[fieldset.component]
    fieldset_spec = fieldset_fn(**kwargs)

    if display_mode == "pdf":
        fieldset_spec.update({
            f'fieldsets/{kwargs["fieldset_name"]}/display/default/el/component': "hidden",
        })
    else:
        fieldset_spec.update({
            f'fieldsets/{kwargs["fieldset_name"]}/display/pdf/el/component': "hidden"
        })

    return fieldset.name, fieldset_spec


def parse_fieldsets(kwargs, context, fieldsets, display_mode="default"):
    fieldset_specs = {}
    parse_objs(
        fieldset_specs, context, fieldsets, parse_fieldset,
        display_mode=display_mode
    )
    kwargs["fieldsets"] = list(
        fieldset_specs.values()
    ) if fieldset_specs else []
