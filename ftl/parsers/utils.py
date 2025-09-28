def parse_objs(kwargs, context, objs, parser, display_mode="default"):
    for obj in objs:
        operator = getattr(obj, "operator", None)
        obj = getattr(obj, "element", obj)
        obj_name, obj_spec = parser(context, obj, display_mode=display_mode)

        keys = obj_name.split("__")
        target = kwargs
        for key in keys[:-1]:
            if key not in target or not isinstance(target[key], dict):
                target[key] = {}
            target = target[key]

        final_key = keys[-1]
        if operator == "-":
            target.pop(final_key, None)
        else:
            target[final_key] = obj_spec


def decide_from_ref_and_orig(obj, orig_obj, attr_name):
    use_orig_attr = getattr(obj, f"edit_{attr_name}", "")
    orig_attr = getattr(orig_obj, attr_name, [])
    attr = getattr(obj, attr_name, [])

    if not attr:
        attr = orig_attr
    elif use_orig_attr:
        attr = orig_attr + attr

    return attr
