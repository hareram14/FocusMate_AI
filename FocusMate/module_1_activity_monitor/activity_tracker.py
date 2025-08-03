import ctypes
import psutil
import pygetwindow as gw
import datetime

def get_pid_from_hwnd(hwnd):
    pid = ctypes.c_ulong()
    ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
    return pid.value

def get_active_window_info():
    try:
        win = gw.getActiveWindow()
        if win:
            hwnd = win._hWnd
            pid = get_pid_from_hwnd(hwnd)
            try:
                process_name = psutil.Process(pid).name()
            except Exception:
                process_name = "Unknown"
            
            window_title = win.title
            
            # Check for ApplicationFrameHost.exe and replace with actual app name based on window title
            if process_name == "ApplicationFrameHost.exe":
                if "WhatsApp" in window_title:
                    process_name = "WhatsApp"
                elif "Microsoft Store" in window_title:
                    process_name = "Microsoft Store"
                # Add more rules here if needed
                
            return {
                "app_name": process_name,
                "window_name": win.title,
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    except Exception as e:
        return {"error": str(e)}
    return None
