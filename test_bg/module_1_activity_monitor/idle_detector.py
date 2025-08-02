from pynput import mouse, keyboard
import time

last_activity_time = time.time()

def update_activity():
    global last_activity_time
    last_activity_time = time.time()

def get_idle_time():
    return time.time() - last_activity_time

def start_listeners():
    mouse.Listener(on_move=lambda *args: update_activity()).start()
    keyboard.Listener(on_press=lambda *args: update_activity()).start()
