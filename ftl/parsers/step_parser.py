from ftl.internal.interface import STEP
from ftl.internal.consent_steps import (
    CONSENT_METHOD,
    OTP,
    GOV_WALLET,
    REJECTED,
)
from ftl.parsers.action_parser import parse_actions
from ftl.parsers.config_parser import parse_config
from ftl.parsers.fieldset_parser import (
    parse_fieldsets
)
from ftl.parsers.utils import decide_from_ref_and_orig


STEP_FN_MAPPING = {
    "INTRO_STEP": STEP,
    "COMMON_STEP_PROPS": STEP,
    "STEP": STEP,
    "CONSENT_METHOD": CONSENT_METHOD,
    "OTP": OTP,
    "GOV_WALLET": GOV_WALLET,
    "REJECTED": REJECTED,
}


def maybe_is_reference(context, step):
    orig_step = step
    update_context = True

    if str(step).startswith('<StepReference'):
        orig_step = context["steps"][step.name]
        if orig_step.step_fn == "COMMON_STEP_PROPS":
            orig_step.step_fn = "STEP"
        if not step.alias:
            update_context = False

    step.name = getattr(step, "alias", step.name) or orig_step.name
    step.step_fn = getattr(orig_step, "step_fn", None)
    step.title = step.title or getattr(orig_step, "title", None)
    step.actions = decide_from_ref_and_orig(step, orig_step, "actions")
    step.fieldsets = decide_from_ref_and_orig(step, orig_step, "fieldsets")
    step.config = decide_from_ref_and_orig(step, orig_step, "config")
    return step, update_context


def pdf_to_context(context, pdf):
    orig_pdf = pdf

    if str(pdf).startswith('<PDFSpecReference'):
        orig_pdf = context["pdfs"][pdf.name]

    pdf.fieldsets = decide_from_ref_and_orig(pdf, orig_pdf, "fieldsets")
    pdf.config = decide_from_ref_and_orig(pdf, orig_pdf, "config")

    context["pdfs"][pdf.name] = pdf
    return pdf


def maybe_step_has_pdf(kwargs, context, step):
    pdf = None
    for action in step.actions:
        action = getattr(action, "element", action)  # maybe mutation
        if action.action_type in ("PDF", "ENTITY_PDF"):
            pdf = action.pdf_spec

    if not pdf:
        return

    pdf = pdf_to_context(context, pdf)

    parse_config(kwargs, context, pdf.config)

    fieldset_specs = {}
    parse_fieldsets(fieldset_specs, context, pdf.fieldsets, display_mode="pdf")
    kwargs["fieldsets"] += fieldset_specs["fieldsets"]


def parse_step(context, step):
    kwargs = {}

    step, update_context = maybe_is_reference(context, step)

    if step.title:
        kwargs["title"] = step.title

    parse_config(kwargs, context, step.config)
    parse_actions(kwargs, context, step.actions)
    parse_fieldsets(kwargs, context, step.fieldsets)
    maybe_step_has_pdf(kwargs, context, step)

    step_fn = STEP_FN_MAPPING[step.step_fn]

    if update_context:
        context["steps"][step.name] = step

    step_spec = step_fn(**kwargs)

    if step.step_fn == "COMMON_STEP_PROPS":
        pass
    elif step.step_fn == "INTRO_STEP":
        context["spec"]["steps_spec"]["intro_step_ns"] = step_spec
    else:
        if not context["spec"]["steps_spec"]["steps_ns"]:
            context["spec"]["steps_spec"]["first_step"] = step.name
        context["spec"]["steps_spec"]["steps_ns"][step.name] = step_spec
