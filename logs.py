import constants
import sys

logging = False if " ".join(sys.argv).find("--logging") == -1 else True
logging_endline = "\n" if logging == True else ""

def start_message():
    print(f"\nWaiting for \"{constants.RECORD_KEY.upper()}\" to start recording...{' (logging enabled)' if logging == True else ''}")

def recording_started():
    print(f"Recording started. You can press \"{constants.STOP_KEY.upper()}\" to stop it...{logging_endline}")

def recording_ended():
    print(f"{logging_endline}Recording finished. You can press \"{constants.PLAY_KEY.upper()}\" to play it, or \"{constants.RECORD_KEY.upper()}\" to record again...")

def macro_empty():
    print(f"Nothing to play. Waiting for \"{constants.RECORD_KEY.upper()}\" to start recording again...")

def playing_started():
    print(f"Playing...{logging_endline}")

def playing_stopped():
    print(f"{logging_endline}Playback finished. Waiting for \"{constants.PLAY_KEY.upper()}\" to play it or \"{constants.RECORD_KEY.upper()}\" to record again...")

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