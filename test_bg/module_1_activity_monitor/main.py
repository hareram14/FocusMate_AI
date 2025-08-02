import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from activity_tracker import get_active_window_info
from idle_detector import get_idle_time, start_listeners
from database import init_db, log_usage
import time

if __name__ == "__main__":
    init_db()
    start_listeners()

    print("🟢 Monitoring started...")

    try:
        while True:
            info = get_active_window_info()
            if info and "error" not in info:
                idle = int(get_idle_time())
                log_usage(info["app_name"], str(info["window_name"]), info["timestamp"], idle)
                print(f"{info['timestamp']} | {info['app_name']} | {info["window_name"]} | Idle: {idle}s")
            time.sleep(5)  # collect every 5 seconds
    except KeyboardInterrupt:
        print("\n✅ Monitoring stopped by user. Data saved to database.")