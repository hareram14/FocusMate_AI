# run_assistant.py
from assistant.recommender import get_recommendations
from assistant.quotes import get_random_quote
from assistant.gpt_assistant import generate_summary  # ✅ Include this
import pandas as pd

CSV_PATH = "outputs/cleaned_logs.csv"

print("🧠 Personalized Assistant\n" + "-"*30)

# Rule-based suggestions
recommendations = get_recommendations(CSV_PATH)
for rec in recommendations:
    print("💡 Suggestion:", rec)

# Motivational quote
quote = get_random_quote()
print("\n🗣️ Quote of the Day:", quote)

# ✅ GPT Summary
try:
    df = pd.read_csv(CSV_PATH)
    print("\n🧾 GPT Summary:")
    print(generate_summary(df))
except Exception as e:
    print("\nGPT Summary skipped:", str(e))
