# analyzer.py
import pandas as pd
from analysis.categorizer import get_app_category

def analyze_productivity(csv_path):
    df = pd.read_csv(csv_path)

    # Add category column
    df['category'] = df['app_name'].apply(get_app_category)

    # Compute stats (optional)
    total_idle_time = df['idle_time'].sum()
    total_logs = len(df)
    active_time = total_logs * 5 - total_idle_time  # Assuming 5s interval

    top_apps = df['app_name'].value_counts().head(5)
    category_usage = df['category'].value_counts()

    summary = {
        "Total Active Time (s)": active_time,
        "Total Idle Time (s)": total_idle_time,
        "Top Apps": top_apps.to_dict(),
        "Category Usage": category_usage.to_dict()
    }

    # Print summary (optional)
    print("\n📊 Summary Statistics")
    print("-" * 30)
    for k, v in summary.items():
        print(f"{k}: {v}")

    # Return DataFrame with 'category' added
    return df
