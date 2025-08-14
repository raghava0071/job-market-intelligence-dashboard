import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("clustered_jobs.csv")

st.title("💼 Job Market Intelligence Dashboard")

# Sidebar filters
st.sidebar.header("Filter Jobs")
selected_cluster = st.sidebar.selectbox("Select Cluster", sorted(df['cluster'].unique()))

# Filter the data
filtered_df = df[df['cluster'] == selected_cluster]

# Display
st.subheader(f"📌 Top Jobs in Cluster {selected_cluster}")
st.dataframe(
    filtered_df[['job_title', 'employer_name', 'job_city']].reset_index(drop=True),
    use_container_width=True
)

with st.expander("📄 View Job Descriptions"):
    for i, row in filtered_df.iterrows():
        st.markdown(f"**{row['job_title']}** at *{row['employer_name']}* ({row['job_city']})")
        st.write(row['job_description'])
        st.markdown("---")


# Optional: Cluster insights
st.write(f"📊 Showing {len(filtered_df)} jobs from this cluster.")

# ===================
# 🔹 Top Skills Chart
# ===================

import ast
from collections import Counter

st.subheader("🔧 Top Skills in Job Descriptions")

# Convert stringified lists back to actual lists
df['skills'] = df['skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else [])

# Flatten and count
all_skills = [skill for skills in df['skills'] for skill in skills]
top_skills = Counter(all_skills).most_common(10)

# Bar chart
if top_skills:
    skill_names, skill_counts = zip(*top_skills)
    fig, ax = plt.subplots(figsize=(8,4))
    ax.bar(skill_names, skill_counts)
    ax.set_title("Top 10 In-Demand Skills")
    ax.set_ylabel("Frequency")
    plt.xticks(rotation=45)
    st.pyplot(fig)
else:
    st.write("No skills found.")
