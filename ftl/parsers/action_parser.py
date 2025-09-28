from ftl.internal.standardized_actions import (
    ACTION_FN_MAPPING
)
from ftl.parsers.config_parser import parse_config
from ftl.parsers.utils import (
    parse_objs,
    decide_from_ref_and_orig
)


def maybe_is_reference(context, action):
    if "PDFAction" in str(action):
        return action, False

    orig_action = action
    update_context = True

    if str(action).startswith('<ActionReference'):
        orig_action = context["actions"][action.name]
        if not action.alias:
            update_context = False

    action.name = getattr(action, "alias", action.name) or orig_action.name
    action.action_type = action.action_type or getattr(
        orig_action, "action_type", None
    )
    action.config = decide_from_ref_and_orig(action, orig_action, "config")

    return action, update_context


def parse_action(context, action, display_mode="default"):
    kwargs = {}

    action, update_context = maybe_is_reference(context, action)
    parse_config(kwargs, context, action.config)

    if update_context:
        context["actions"][action.name] = action

    action_fn = ACTION_FN_MAPPING[action.action_type]
    action_spec = action_fn(**kwargs)

    return action.action_type, action_spec


def parse_actions(kwargs, context, actions, display_mode="default"):
    action_specs = {}
    parse_objs(
        action_specs, context, actions, parse_action, display_mode=display_mode
    )
    kwargs["actions"] = list(action_specs.values()) if action_specs else []
