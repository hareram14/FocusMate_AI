# run_analysis.py
from analysis.analyzer import analyze_productivity
from analysis.visualizer import plot_category_pie, plot_hourly_heatmap


CSV_PATH = "outputs/cleaned_logs.csv"

summary = analyze_productivity(CSV_PATH)
summary.to_csv(CSV_PATH, index=False)

print("\n📊 Productivity Summary:")
for key, value in summary.items():
    print(f"{key}: {value}")

plot_category_pie(CSV_PATH)
plot_hourly_heatmap(CSV_PATH)
