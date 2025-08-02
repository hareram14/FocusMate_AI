import time
from module_6_focus_mode.notifier import send_notification

def start_timer(minutes):
    seconds = minutes * 60
    for remaining in range(seconds, 0, -1):
        if remaining % 60 == 0:
            print(f"⏳ Time left: {remaining // 60} min")
        time.sleep(1)
    send_notification("Focus Mode", "Time's up! Great job!")
