import os
import sqlite3

def init_db():
    # Get the absolute path to the 'data' folder (relative to this script)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, '..', 'data', 'usage_logs.db')
    db_path = os.path.normpath(db_path)  # Normalize path (especially for Windows)

    # Make sure the directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # Connect and initialize DB
    conn = sqlite3.connect('data/usage_logs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usage (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        app_name TEXT,
        window_name TEXT,
        timestamp TEXT,
        idle_time INTEGER
    )''')
    conn.commit()
    conn.close()

def log_usage(app_name, window_name, timestamp, idle_time):
    conn = sqlite3.connect('data/usage_logs.db')
    c = conn.cursor()
    c.execute('INSERT INTO usage (app_name, window_name, timestamp, idle_time) VALUES (?, ?, ?, ?)',
              (app_name, window_name, timestamp, idle_time))
    conn.commit()
    conn.close()
