import keyboard
import listeners
import constants
import util
import logs

try:
    listeners.attach_hooks()
    logs.start_message()
    keyboard.wait()
except KeyboardInterrupt:
    util.clear_all()