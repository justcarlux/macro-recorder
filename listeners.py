import keyboard
import mouse
import constants
from play import play_macro
import util
import logs

recording = False
playing = False
macro = []

record_key_released = False
last_key_event = None

def keyboard_hook_callback(event):

    global recording
    global record_key_released
    global macro
    global playing
    global last_key_event

    if (playing == True): return
    if (isinstance(event, keyboard.KeyboardEvent)):

        if (
            (recording == False) and
            (event.scan_code == keyboard.key_to_scan_codes(constants.RECORD_KEY)[0])
        ):
            
            macro = []
            macro.append({
                "name": "started",
                "event": None,
                "time": event.time
            })
            record_key_released = False
            recording = True
            logs.recording_started()
            
        elif recording == True:

            if (event.scan_code == keyboard.key_to_scan_codes(constants.STOP_KEY)[0]):
                recording = False
                logs.recording_ended()
                return
            
            if (
                (event.event_type == "up") and
                (event.scan_code == keyboard.key_to_scan_codes(constants.RECORD_KEY)[0])
            ):
                record_key_released = True
                return
            
            if (
                (last_key_event) and
                (last_key_event.scan_code == event.scan_code) and
                (last_key_event.event_type == event.event_type)
            ): return
            
            data = { "name": event.name, "event_type": event.event_type, "scan_code": event.scan_code }
            logs.key(data, True)
            macro.append({
                "name": "keyboard",
                "event": data,
                "time": event.time
            })
            last_key_event = event

        if (
            (playing == False) and
            (recording == False) and
            (event.event_type == "up") and
            (event.scan_code == keyboard.key_to_scan_codes(constants.PLAY_KEY)[0])
        ):
            if (len(macro) == 1):
                logs.macro_empty()
                return
            logs.playing_started()
            playing = True
            play_macro(macro)
            playing = False
            util.release_macro_keys(macro)
            util.release_mouse_buttons()
            logs.playing_stopped()
        
def mouse_hook_callback(event):

    global last_mouse_event
    entry = { "time": event.time }

    if (recording == False): return
    if (isinstance(event, mouse.ButtonEvent)):
        if (event.button not in constants.CLICKS_NAMES): return
        event_type = "down" if event.event_type == "double" else event.event_type
        data = { "event_type": event_type, "button": event.button }
        logs.mouse_click(data, True)
        entry["name"] = "mouse-button"
        entry["event"] = data
    elif (isinstance(event, mouse.MoveEvent)):
        data = { "x": event.x, "y": event.y }
        logs.mouse_move(data, True)
        entry["name"] = "mouse-move"
        entry["event"] = data
    elif (isinstance(event, mouse.WheelEvent)):
        data = { "delta": event.delta }
        logs.mouse_wheel(data, True)
        entry["name"] = "mouse-wheel"
        entry["event"] = data

    macro.append(entry)

def attach_hooks():
    keyboard.hook(keyboard_hook_callback)
    mouse.hook(mouse_hook_callback)