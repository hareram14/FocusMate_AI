# dashboard/visual_utils.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style="whitegrid")

def load_data(csv_path):
    return pd.read_csv(csv_path)

def plot_app_usage(df):
    st.subheader("📊 Top Used Apps")
    app_counts = df['app_name'].value_counts().head(10)

    fig, ax = plt.subplots()
    sns.barplot(
        x=app_counts.values,
        y=app_counts.index,
        ax=ax,
        hue=app_counts.index,
        palette="viridis",
        legend=False
    )
    ax.set_xlabel("Usage Count")
    ax.set_ylabel("App Name")
    st.pyplot(fig)


def plot_focus_vs_distraction(df):
    st.subheader("🧠 Focus vs Distraction")

    # Ensure 'category' column is lowercase and cleaned
    df['category'] = df['category'].str.strip().str.lower()

    focus_count = (df['category'] == 'focus').sum()
    distraction_count = (df['category'] == 'distraction').sum()
    other_count = len(df) - (focus_count + distraction_count)

    labels = []
    sizes = []
    colors = []

    if focus_count > 0:
        labels.append("Focus")
        sizes.append(focus_count)
        colors.append("#66c2a5")  # greenish
    if distraction_count > 0:
        labels.append("Distraction")
        sizes.append(distraction_count)
        colors.append("#fc8d62")  # orange
    if other_count > 0:
        labels.append("Other")
        sizes.append(other_count)
        colors.append("#8da0cb")  # blue

    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(
        sizes, labels=labels, autopct='%1.1f%%',
        startangle=90, colors=colors, textprops={'fontsize': 12}
    )

    ax.axis('equal')  # Equal aspect ratio ensures a perfect circle
    st.pyplot(fig)

def category_pie(df):
    cat_counts = df['category'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(cat_counts, labels=cat_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
    ax.set_title("App Category Distribution")
    st.pyplot(fig)

def interactive_daily_focus_chart(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date
    df['score'] = df['category'].apply(lambda x: 1 if x == 'Work/Productive' else (-1 if x == 'Distraction' else 0))
    daily_scores = df.groupby('date')['score'].sum().reset_index()

    st.line_chart(daily_scores.rename(columns={"date": "index", "score": "Focus Score"}).set_index("index"))
    st.markdown("<i>Note: Higher scores indicate more productive days.</i>", unsafe_allow_html=True)
