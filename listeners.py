import keyboard
import mouse
import constants
from play import play_macro
import logs
import save_load

recording = False
playing = False
saving_or_loading = False
macro = []
repeat = False

record_key_released = False
last_key_event = None

def keyboard_hook_callback(event):

    global recording
    global record_key_released
    global macro
    global playing
    global last_key_event
    global saving_or_loading
    global repeat

    if (saving_or_loading == True): return
    if (isinstance(event, keyboard.KeyboardEvent) == False): return

    if (
        (recording == False) and
        (event.scan_code == keyboard.key_to_scan_codes(constants.REPEAT_KEY)[0]) and
        (event.event_type == "up")
    ):
        repeat = not repeat
        logs.repeat_toggled()

    if (playing == True): return

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

    elif (
        (recording == False) and
        (event.scan_code == keyboard.key_to_scan_codes(constants.SAVE_KEY)[0]) and
        (event.event_type == "up")
    ):
        saving_or_loading = True
        save_load.save()
        saving_or_loading = False

    elif (
        (recording == False) and
        (event.scan_code == keyboard.key_to_scan_codes(constants.LOAD_KEY)[0]) and
        (event.event_type == "up")
    ):
        saving_or_loading = True
        save_load.load()
        saving_or_loading = False
            
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
        play_macro()
        
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