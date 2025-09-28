from ftl.internal.interface import (
    TEMPLATE, STEPS_SPEC
)
from ftl.parsers.config_parser import parse_config


def parse_template(context, template):
    template_spec = {}
    steps_spec = context["spec"]["steps_spec"]
    parse_config(template_spec, context, template.config)

    if "collectable" in template_spec:
        steps_spec["collectable"] = template_spec.pop("collectable")
    if "sign" in template_spec:
        steps_spec["sign"] = template_spec.pop("sign")
    if "scoped_permission_hook" in template_spec:
        steps_spec["scoped_permission_hook"] = template_spec.pop(
            "scoped_permission_hook"
        )

    steps_spec = STEPS_SPEC(**steps_spec)
    template_spec["steps_spec"] = steps_spec
    context["spec"] = TEMPLATE(**template_spec)
