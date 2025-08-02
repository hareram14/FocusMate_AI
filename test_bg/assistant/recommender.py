import pandas as pd
from datetime import timedelta

def get_recommendations(csv_path):
    df = pd.read_csv(csv_path, parse_dates=['timestamp'])

    # Basic daily analysis
    df['date'] = df['timestamp'].dt.date
    daily = df.groupby('date').size()

    # Focus streak suggestion (e.g., >1 hr productive = suggest break)
    recommendations = []
    chunk = pd.Timedelta(minutes=5)

    focus_time = df[df['category'] == 'Productive'].shape[0] * chunk

    if focus_time > timedelta(hours=1):
        recommendations.append("👀 You've focused for over an hour. Time for a short break!")
    elif focus_time < timedelta(minutes=30):
        recommendations.append("🟡 You might want to refocus and limit distractions.")
    else:
        recommendations.append("🟢 Great job staying focused! Keep it up!")

    return recommendations
