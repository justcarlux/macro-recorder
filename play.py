import keyboard
import mouse
from time import time
import logs

def play_macro(macro):

    macro_copy = macro.copy()
    started_time = time()
    macro_started_time = macro_copy[0]["time"]
    macro_copy.pop(0)

    while True:

        if (len(macro_copy) == 0):
            break 
        current_time = time() - started_time
        macro_current_event_time = macro_copy[0]["time"] - macro_started_time

        if (current_time >= macro_current_event_time):

            name = macro_copy[0]["name"]
            event = macro_copy[0]["event"]
            
            match name:
                case "keyboard":
                    keyboard.send(event["scan_code"], event["event_type"] == "down", event["event_type"] == "up")
                    logs.key(event, False)
                case "mouse-button":
                    if (event["event_type"] == "down"):
                        mouse.press(event["button"])
                    else:
                        mouse.release(event["button"])
                    logs.mouse_click(event, False)
                case "mouse-move":
                    mouse.move(event["x"], event["y"])
                    logs.mouse_move(event, False)
                case "mouse-wheel":
                    mouse.wheel(event["delta"])
                    logs.mouse_wheel(event, False)
                
            macro_copy.pop(0)