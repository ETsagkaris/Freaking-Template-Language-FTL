from ftl.parsers.utils import parse_objs


def parse_param(context, param, display_mode="default"):
    variable = context.get("variables", {}).get(param.value)
    if variable:
        param.value = variable.value

    key = param.key
    value = getattr(param.value, "values", param.value)  # perhaps it is a list
    return key, value


def parse_config(kwargs, context, config, display_mode="default"):
    parse_objs(kwargs, context, config, parse_param, display_mode=display_mode)
