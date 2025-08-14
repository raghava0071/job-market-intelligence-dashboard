import pandas as pd
import re
from collections import Counter

df = pd.read_csv("cleaned_jobs.csv")

# Simple skill list for demo (can be expanded or loaded from a file)
skills_list = [
    'python', 'sql', 'excel', 'tableau', 'power bi', 'aws', 'spark',
    'hadoop', 'google analytics', 'machine learning', 'deep learning',
    'nlp', 'data visualization', 'pandas', 'numpy', 'matplotlib'
]

def extract_skills(text):
    text = text.lower()
    found = [skill for skill in skills_list if skill in text]
    return found

df['skills'] = df['job_description'].apply(extract_skills)

# Flatten skills list for top overall skills
flat_skills = [skill for sublist in df['skills'] for skill in sublist]
top_skills = Counter(flat_skills).most_common(15)

print("📌 Top Skills Found:")
for skill, count in top_skills:
    print(f"{skill}: {count}")

df.to_csv("cleaned_jobs.csv", index=False)
