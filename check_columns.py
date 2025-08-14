import pandas as pd

df = pd.read_csv("cleaned_jobs.csv")
print("🧾 Columns in cleaned_jobs.csv:")
print(df.columns.tolist())
