import keyboard
import mouse

def clear_all():
    keyboard.unhook_all()
    mouse.unhook_all()

def release_macro_keys(macro):
    for element in macro:
        if (element["name"] != "keyboard"): continue
        if (keyboard.is_pressed(element["event"]["scan_code"])):
            keyboard.release(element["event"]["scan_code"])

def release_mouse_buttons():
    if (mouse.is_pressed("left")): mouse.release("left")
    if (mouse.is_pressed("right")): mouse.release("right")
    if (mouse.is_pressed("middle")): mouse.release("middle")