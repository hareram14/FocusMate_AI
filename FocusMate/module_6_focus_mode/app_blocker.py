import os
import time
import psutil

def block_apps(app_names):
    print("Blocking apps:", app_names)
    blocked = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            proc_name = proc.info['name'].lower()
            for app in app_names:
                if app.lower() == proc_name:
                    proc.kill()
                    blocked.append(proc_name)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    if blocked:
        print(f"🔒 Blocked apps: {set(blocked)}")
    else:
        print("✅ No running blocked apps were found.")

def unblock_apps(app_names):
    print("Unblock logic can go here (if needed)")
    # Optionally log allowed apps again or alert the user

