from plyer import notification

def send_notification(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            timeout=10  # seconds
        )
    except Exception as e:
        print("Notification Error:", e)
