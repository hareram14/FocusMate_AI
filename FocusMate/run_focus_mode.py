from module_6_focus_mode.focus_controller import start_focus_session

# Replace these with actual app process names from Task Manager if needed
apps_to_block = ['brave.exe','steam.exe', 'spotify.exe']

# Start a 25-minute focus session
start_focus_session(duration_minutes=4, apps_to_block=apps_to_block)
