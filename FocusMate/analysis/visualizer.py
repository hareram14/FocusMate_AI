# visualizer.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from analysis.categorizer import get_app_category

def plot_category_pie(csv_path):
    df = pd.read_csv(csv_path)
    df['category'] = df['app_name'].apply(get_app_category)
    category_counts = df['category'].value_counts()

    plt.figure(figsize=(6,6))
    category_counts.plot.pie(autopct='%1.1f%%')
    plt.title("App Usage by Category")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

def plot_hourly_heatmap(csv_path):
    df = pd.read_csv(csv_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    df['day'] = df['timestamp'].dt.day_name()

    heatmap_data = df.groupby(['day', 'hour']).size().unstack().fillna(0)
    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_data, cmap="YlGnBu", linewidths=.5)
    plt.title("Activity Heatmap by Hour and Day")
    plt.xlabel("Hour of Day")
    plt.ylabel("Day of Week")
    plt.tight_layout()
    plt.show()
