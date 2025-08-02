import sqlite3
import pandas as pd
import os

# Step 1: Load data
def load_data():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'usage_logs.db')
    db_path = os.path.normpath(db_path)

    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM usage", conn)
    conn.close()
    return df

# Step 2: Clean and normalize data
def clean_data(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Drop rows with missing app/window name
    df.dropna(subset=['app_name', 'window_name'], inplace=True)

    # Remove idle entries (> 60s)
    df = df[df['idle_time'] <= 60]

    # Add time chunks (e.g., every 5 minutes)
    df['time_chunk'] = df['timestamp'].dt.floor('5min')

    return df

# Step 3: Save cleaned data to CSV
def save_to_csv(df):
    output_path = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'cleaned_logs.csv')
    output_path = os.path.normpath(output_path)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"[INFO] Cleaned data saved to {output_path}")

# Final runner
if __name__ == "__main__":
    df = load_data()
    df_cleaned = clean_data(df)
    save_to_csv(df_cleaned)

    print("\n[INFO] Sample cleaned data:")
    print(df_cleaned.head())
