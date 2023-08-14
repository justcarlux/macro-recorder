import keyboard
import listeners
import util
import logs
import save_load

try:
    save_load.init_saves_folder()
    listeners.attach_hooks()
    logs.start_message()
    keyboard.wait()
except KeyboardInterrupt:
    util.clear_all()