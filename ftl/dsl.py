from textx import metamodel_from_str
import argparse
import os
import sys
import json

curr_path = os.path.dirname(os.path.realpath(__file__))
ftl_path = os.path.dirname(curr_path)
sys.path.append(ftl_path)


ftl_grammar = """
Model: commands*=Command;

Command:
    Template | VariableAssignment | PDFSpecDefinition| Step ;

VariableAssignment:
    name=ID '=' value=VariableValue ';';

VariableValue:
    STRING | INT | FLOAT | BOOL;

Component:
    'FIELDSET' | 'FORM' | 'VIEW' | 'TABLE' | 'FOOTNOTES' | 'HEADER'
    | 'DOC_TITLE' | 'SIGNATURE';

Datatype:
    'FIELD' | 'RECIPIENT' | 'INFO' | 'TEXT' | 'STRING' | 'EMAIL' | 'DATE'
    | 'AFM' | 'PHONE' | 'MOBILE' | 'IBAN' | 'ATTACHMENT'
    | 'RADIO_CHOICE' | 'CHOICE' | 'HIERARCHICAL_SELECTOR'
    | 'TITLE' | 'SUBTITLE' | 'REFCODE' | 'EMBLEM' | 'INT'
    | 'SIGN_DATE' | 'SIGNER_TITLE' | 'SIGNER_EMPTY' | 'SIGNER_NAME';

InputMode:
    'REQUIRED' | 'OPTIONAL' | 'NOINPUT' | 'DISPLAY';


Template:
    'TEMPLATE'
    '{' config+=ConfigEntry+ '}'
    ';';

StepFn:
    'STEP'| 'INTRO_STEP' | 'COMMON_STEP_PROPS' | 'OTP';


Step:
    StepDefinition | StepReference;

StepDefinition:
    step_fn=StepFn
    title=STRING?
    ('(' actions+=Action+ ')')?
    ('[' fieldsets+=Fieldset+ ']')?
    ('{' config+=ConfigEntry+ '}')?
    'as' name=ID
    ';';

StepReference:
    name=ID
    (title=STRING)?
    (edit_actions='edit'? '(' actions+=MutationAction+ ')')?
    (edit_fieldsets='edit'? '[' fieldsets+=MutationFieldset+ ']')?
    (edit_config='edit'? '{' config+=MutationConfig+ '}')?
    ('as' alias=ID)?
    ';';


PDFSpec:
    PDFSpecDefinition | PDFSpecReference;

PDFSpecDefinition:
    "PDF_SPEC"
    '[' fieldsets+=Fieldset+ ']'
    ('{' config+=ConfigEntry+ '}')?
    'as' name=ID
    ';';

PDFSpecReference:
    name=ID ';';


Fieldset:
    FieldsetDefinition | FieldsetReference;

FieldsetDefinition:
    component=Component
    title=STRING?
    ('[' fields+=Field+ ']')?
    ('{' config+=ConfigEntry+ '}')?
    'as' name=ID
    ';';

FieldsetReference:
    (component=Component)?
    name=ID
    (title=STRING)?
    (edit_fields='edit'? '[' fields+=MutationField+ ']')?
    (edit_config='edit'? '{' config+=MutationConfig+ '}')?
    ('as' alias=ID)?
    ';';


Field:
    FieldDefinition | FieldReference;

FieldDefinition:
    datatype=Datatype
    input_mode=InputMode?
    title=STRING?
    ('[' choices+=ConfigEntry+ ']')?
    ('{' config+=ConfigEntry+ '}')?
    'as' name=ID
    ';';

FieldReference:
    (datatype=Datatype)?
    (input_mode=InputMode)?
    name=ID
    (title=STRING)?
    (edit_config='edit'? '{' config+=MutationConfig+ '}')?
    ('as' alias=ID)?
    ';';


Action:
    OtherAction | PDFAction;


OtherAction:
    ΑctionDefinition | ActionReference;

ΑctionDefinition:
    action_type=ActionType
    ('{' config+=ConfigEntry+ '}')?
    'as' name=ID
    ';';

ActionReference:
    (action_type=ActionType)?
    name=ID
    (edit_config='edit'? '{' config+=MutationConfig+ '}')?
    ('as' alias=ID)?
    ';';

ActionType:
    /[A-Z_]+/;

PDFAction:
    action_type=PDFActionType '(' pdf_spec=PDFSpec ')'
    ('{' config+=ConfigEntry+ '}')?
    ';';

PDFActionType:
    'PDF' | 'ENTITY_PDF';


ListValue:
    '[' values+=VariableValue[','] ']';

ConfigValue:
    STRING | INT | FLOAT | BOOL | ListValue | ID;


ConfigEntry:
    key=ID ('=' value=ConfigValue)? ';';

MutationAction:
    operator='-'? element=Action;
MutationFieldset:
    operator='-'? element=Fieldset;
MutationField:
    operator='-'? element=Field;
MutationConfig:
    operator='-'? element=ConfigEntry;

Comment: /#.*$/;
"""

META_MODEL = metamodel_from_str(ftl_grammar)


def handle_comand(context, command):
    from ftl.parsers import (
        step_parser,
        template_parser
    )

    if str(command).startswith('<VariableAssignment'):
        context["variables"][command.name] = command
        return

    if (
        str(command).startswith('<StepDefinition') or
        str(command).startswith('<StepReference')
    ):
        step_parser.parse_step(context, command)
        return

    if str(command).startswith('<PDFSpecDefinition'):
        step_parser.pdf_to_context(context, command)
        return

    if (
        "Template" in str(command)
    ):
        template_parser.parse_template(context, command)
        return

    return


def parse(ftl_script):

    model = META_MODEL.model_from_str(ftl_script)
    context = {
        "variables": {},
        "pdfs": {},
        "steps": {},
        "fieldsets": {},
        "fields": {},
        "actions": {},
        "spec": {
            "steps_spec": {
                "first_step": None,
                "intro_step_ns": None,
                "steps_ns": {},
            }
        }
    }
    for command in model.commands:
        handle_comand(context, command)
    return context["spec"]


def cli_script(filepath):
    with open(filepath, "r") as f:
        ftl_script = f.read()

    print("PARSING:")
    print(ftl_script)

    template_spec = parse(ftl_script)
    print("FINISHED")
    filename = template_spec["refname"] + ".json"
    with open(filename, "w") as f:
        print(f"SAVE TO: {filename}")
        f.write(json.dumps(
            template_spec, ensure_ascii=False,
            indent=2
        ))


parser = argparse.ArgumentParser(description="Parses ftl files")
parser.add_argument(
    "filepath",
    help="filepath to parse",
)

if __name__ == "__main__":
    args = parser.parse_args()
    cli_script(args.filepath)
