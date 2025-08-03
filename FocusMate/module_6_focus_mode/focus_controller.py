import time
from module_6_focus_mode.timer import start_timer
from module_6_focus_mode.app_blocker import block_apps, unblock_apps
from module_6_focus_mode.notifier import send_notification


def start_focus_session(duration_minutes=4, apps_to_block=[]):
    print(f"🧘 Starting Focus Mode for {duration_minutes} minutes...")
    send_notification("🧘 Focus Mode Started", f"Stay focused for {duration_minutes} minutes!")

    for minute in range(duration_minutes, 0, -1):
        block_apps(apps_to_block)  # Actively monitor and kill
        print(f"⏳ Time left: {minute} min")
        time.sleep(60)  # Wait a minute before checking again

    send_notification("🎉 Focus Session Complete", "You can now take a break!")
    print("🎉 Focus Mode complete. Good job!")
