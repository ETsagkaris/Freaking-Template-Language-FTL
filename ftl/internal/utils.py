def get_fieldset_name(fieldset):
    for key in fieldset.keys():
        if key.startswith("fieldsets/"):
            return key.split("/")[1]


def add_fieldsets(step, step_type, fieldsets):
    if step_type:
        assert step_type in ("form", "view")
        web_component = "form" if step_type == "form" else "values-list"
    for fieldset in fieldsets:
        fieldset_name = get_fieldset_name(fieldset)
        pdf_component = fieldset.get(
            f"fieldsets/{fieldset_name}/display/pdf/el/component",
            "table"
        )

        step["fieldset-order"].append(fieldset_name)
        step.update(fieldset)
        if step_type:
            step.update({
                f"fieldsets/{fieldset_name}/display/default/el/component": (
                    web_component),
                f"fieldsets/{fieldset_name}/display/pdf/el/component": (
                    pdf_component
                ),
            })
    step["fieldset-order"] = " ".join(step["fieldset-order"])


def add_action(step, action_spec):
    step.update(action_spec)
    action_name = list(action_spec.keys())[0].split("/")[1]
    step["action-order"].append(action_name)


def add_actions(step, actions):
    for action in actions:
        add_action(step, action)
    step["action-order"] = " ".join(step["action-order"])


def add_next_step_spec(
    step_ns, next_step, decide_next_step, possible_next_steps
):
    if next_step:
        step_ns["next_step"] = next_step
        return

    if decide_next_step:
        assert possible_next_steps
        step_ns["decide_next_step"] = decide_next_step
        for name in possible_next_steps:
            step_ns[f"possible_next_steps/{name}/documentation/label"] = name
        return
    return


def fillChoice(nsdata, field_name, options, mode='default', lang='el'):
    component_key = '/'.join(
        ['fields', field_name, 'display', mode, lang, 'component']
    )
    assert nsdata[component_key].endswith('choice')
    keys = []
    for option in options:
        key_val, option = option
        key = '/'.join([
            'fields', field_name, 'display', mode, lang, 'choices', key_val
        ])
        nsdata[key] = option
        keys.append(key_val)
    choices_order_key = '/'.join([
        'fields', field_name, 'display', mode, lang, 'choices-order'
    ])
    nsdata[choices_order_key] = ' '.join(keys)


def ensure_no_input_fields(step):
    for key, value in step.items():
        if key.startswith('fields/') and key.endswith('/user-input-mode'):
            if value not in ['noinput', 'display']:
                step[key] = 'noinput'


def update_doc(doc, elems, value):
    if not elems:
        return value
    head = elems[0]
    tail = elems[1:]
    subdoc = doc.get(head, {})
    doc[head] = update_doc(subdoc, tail, value)
    return doc


def namespace_to_doc(nsdata):
    doc: dict = {}
    for key, value in nsdata.items():
        elems = key.split("/")
        update_doc(doc, elems, value)
    return doc
