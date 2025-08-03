# categorizer.py

def get_app_category(app_name):
    categories = {
        "code.exe": "Work",
        "chrome.exe": "Browsing",
        "firefox.exe": "Browsing",
        "explorer.exe": "File Management",
        "outlook.exe": "Communication",
        "whatsapp.exe": "Communication",
        "teams.exe": "Communication",
        "vlc.exe": "Entertainment",
        "spotify.exe": "Entertainment",
        "notepad.exe": "Note Taking",
        "excel.exe": "Work",
        "word.exe": "Work",
        "powerpnt.exe": "Work",
    }

    if not isinstance(app_name, str):
        return "Others"

    return categories.get(app_name.lower(), "Others")
