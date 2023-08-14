import keyboard
import mouse
from time import time
import logs
import listeners
import util
import threading

def play_macro():

    if (len(listeners.macro) < 2):
        logs.play_macro_empty()
        return
    
    logs.playing_started()

    def worker():
        
        listeners.playing = True
        macro_copy = listeners.macro.copy()
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
        
        util.release_macro_keys()
        util.release_mouse_buttons()
        logs.playing_stopped()
        listeners.playing = False
        if listeners.repeat: worker()
        return
    
    thread = threading.Thread(target=worker)
    thread.start()