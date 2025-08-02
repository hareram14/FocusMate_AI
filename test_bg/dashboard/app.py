# dashboard/app.py
import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dashboard.visual_utils import (
    load_data, plot_app_usage, plot_focus_vs_distraction, category_pie, interactive_daily_focus_chart
)

st.set_page_config(page_title="FocusMate AI Dashboard", layout="wide")

st.title("📊 FocusMate AI Dashboard")
st.markdown("Welcome to your personal productivity dashboard powered by **FocusMate AI**.")

# Load data
df = load_data("outputs/cleaned_logs.csv")

# Dashboard Layout
col1, col2 = st.columns(2)

with col1:
    st.header("📈 App Usage")
    plot_app_usage(df)

with col2:
    st.header("🧠 Focus vs Distraction")
    plot_focus_vs_distraction(df)

st.header("🧩 App Category Overview")
category_pie(df)

st.header("📅 Daily Focus Trends")
interactive_daily_focus_chart(df)
