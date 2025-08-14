import pandas as pd
import re

# Load the raw job data
df = pd.read_csv("raw_jobs.csv")

# Show basic info
print("📊 Number of jobs collected:", len(df))
print("\n📄 Column names:\n", df.columns.tolist())

# Let's preview a few job descriptions
print("\n📝 Sample job descriptions:\n", df['job_description'].head(2))

# Clean the job descriptions
def clean_text(text):
    if pd.isna(text):
        return ""
    text = re.sub(r"http\S+", "", text)  # remove links
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # remove punctuation/numbers
    text = text.lower()  # lowercase
    text = re.sub(r"\s+", " ", text).strip()  # remove extra spaces
    return text

df["clean_description"] = df["job_description"].apply(clean_text)

# Save cleaned data
df.to_csv("cleaned_jobs.csv", index=False)
print("✅ Cleaned job data saved to cleaned_jobs.csv")
