import constants
import sys
import listeners

logging = False if " ".join(sys.argv).find("--logging") == -1 else True
logging_endline = "\n" if logging == True else ""

def start_message():
    print(f"\nWelcome. Press \"{constants.RECORD_KEY.upper()}\" to start recording or \"{constants.LOAD_KEY.upper()}\" to load a previously saved macro.{' (logging enabled)' if logging == True else ''}")

def recording_started():
    print(f"Recording started. Press \"{constants.STOP_KEY.upper()}\" to stop.{logging_endline}")

def recording_ended():
    print(f"{logging_endline}Recording finished. Press \"{constants.PLAY_KEY.upper()}\" to play, \"{constants.RECORD_KEY.upper()}\" to record again, \"{constants.SAVE_KEY.upper()}\" to save or \"{constants.LOAD_KEY.upper()}\" to load a previously saved macro.")

def play_macro_empty():
    print(f"Nothing to play. Press \"{constants.RECORD_KEY.upper()}\" to start recording or \"{constants.LOAD_KEY.upper()}\" to load a previously saved macro.")

def playing_started():
    print(f"Playing...{logging_endline}")

def playing_stopped():
    print(f"{logging_endline}Playback finished. Press \"{constants.PLAY_KEY.upper()}\" to play, \"{constants.RECORD_KEY.upper()}\" to record again, \"{constants.SAVE_KEY.upper()}\" to save or \"{constants.LOAD_KEY.upper()}\" to load a previously saved macro.")

def key(event, recording):
    if (logging == False): return
    type = "Recorded" if recording == True else "Played"
    print(f"- ({type}) {constants.KEYBOARD_TYPES[event['event_type']]}: {event['name']} (Code: {event['scan_code']})")

def mouse_click(event, recording):
    if (logging == False): return
    type = "Recorded" if recording == True else "Played"
    print(f"- ({type}) {constants.CLICKS_NAMES[event['button']]} {constants.MOUSE_TYPES[event['event_type']]}")

def mouse_move(event, recording):
    if (logging == False): return
    type = "Recorded" if recording == True else "Played"
    print(f"- ({type}) Mouse movement. X: {event['x']} - Y: {event['y']}")

def mouse_wheel(event, recording):
    if (logging == False): return
    type = "Recorded" if recording == True else "Played"
    print(f"- ({type}) Mouse wheel. Delta: {event['delta']}")

SAVE_PROMPT = "Write a name for your macro: "
SAVE_PROMPT_INVALID_NAME = "Please write a valid name for your macro (can only contain letters and numbers, no spaces and symbols): "
def save_prompt_already_existent_macro(name):
    return f"There is already another saved macro called \"{name}\". Write another one: "

def save_macro_empty():
    print(f"Nothing to save. Press \"{constants.RECORD_KEY.upper()}\" to start recording.")

def error_saving_macro(ex):
    print(f"An error ocurred when saving the macro file: {str(ex)}. Press \"{constants.PLAY_KEY.upper()}\" to play, \"{constants.RECORD_KEY.upper()}\" to record again, \"{constants.SAVE_KEY.upper()}\" to save or \"{constants.LOAD_KEY.upper()}\" to load a previously saved macro.")

def saved_macro():
    print(f"Your macro has been saved. Press \"{constants.PLAY_KEY.upper()}\" to play, \"{constants.RECORD_KEY.upper()}\" to record again, \"{constants.SAVE_KEY.upper()}\" to save or \"{constants.LOAD_KEY.upper()}\" to load a previously saved macro.")

LOAD_PROMPT = "Write the name of the macro you want to load: "

def load_unexistent_macro():
    if (len(listeners.macro) < 2):
        print(f"There is not a macro with that name. Press \"{constants.RECORD_KEY.upper()}\" to start recording or \"{constants.LOAD_KEY.upper()}\" to load a previously saved macro.")
    else:
        print(f"There is not a macro with that name. Press \"{constants.PLAY_KEY.upper()}\" to play, \"{constants.RECORD_KEY.upper()}\" to record again, \"{constants.SAVE_KEY.upper()}\" to save or \"{constants.LOAD_KEY.upper()}\" to load a previously saved macro.")

def load_macro_error(ex):
    if (len(listeners.macro) < 2):
        print(f"An error ocurred when loading the macro file: {str(ex)}. Press \"{constants.RECORD_KEY.upper()}\" to start recording or \"{constants.LOAD_KEY.upper()}\" to load a previously saved macro.")
    else:
        print(f"An error ocurred when loading the macro file: {str(ex)}. Press \"{constants.PLAY_KEY.upper()}\" to play, \"{constants.RECORD_KEY.upper()}\" to record again, \"{constants.SAVE_KEY.upper()}\" to save or \"{constants.LOAD_KEY.upper()}\" to load a previously saved macro.")

def loaded_macro(name):
    print(f"Macro \"{name}\" has been loaded. Press \"{constants.PLAY_KEY.upper()}\" to play, \"{constants.RECORD_KEY.upper()}\" to record again, \"{constants.SAVE_KEY.upper()}\" to save or \"{constants.LOAD_KEY.upper()}\" to load a previously saved macro.")