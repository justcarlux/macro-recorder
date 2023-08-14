import listeners
import os
import re
import logs
import json
import sys

def init_saves_folder():
    if (os.path.exists("saves") == False):
        os.mkdir("saves")

save_regex = re.compile(r"[a-zA-Z0-9]", flags=re.IGNORECASE)
def save():

    if (len(listeners.macro) < 2):
        logs.save_macro_empty()
        return
    name = ""
    valid_name = False
    prompt = logs.SAVE_PROMPT
    while valid_name == False:
        name = input(prompt)
        if (len(save_regex.findall(name)) != len(name)):
            prompt = logs.SAVE_PROMPT_INVALID_NAME
        elif (os.path.exists(f"saves/{name}.json")):
            prompt = logs.save_prompt_already_existent_macro(name)
        else:
            valid_name = True

    try:
        with open(f"saves/{name}.json", "w") as f:
            f.write(json.dumps(listeners.macro))
    except Exception as ex:
        logs.error_saving_macro(ex)
        return

    logs.saved_macro()

def load():
    name = input(logs.LOAD_PROMPT)
    if (os.path.exists(f"saves/{name}.json")):
        try:
            with open(f"saves/{name}.json", "r") as f:
                data = json.load(f)
                if (len(data) < 2): raise Exception("Macro empty")
                listeners.macro = data
                logs.loaded_macro(name)
        except Exception as ex:
            logs.load_macro_error(ex)
    else:
        logs.load_unexistent_macro()