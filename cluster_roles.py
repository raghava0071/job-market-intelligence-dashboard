import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Load cleaned data
df = pd.read_csv("cleaned_jobs.csv")

# Ensure column is named correctly
df['clean_description'] = df['clean_description'].fillna("")

# Vectorize
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['clean_description'])

# KMeans clustering
k = 5
kmeans = KMeans(n_clusters=k, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

# Save the updated file
df.to_csv("clustered_jobs.csv", index=False)

# Optional: Show a few examples
for cluster_num in range(k):
    print(f"\n🔹 Cluster {cluster_num}")
    display = df[df['cluster'] == cluster_num][['job_title', 'employer_name', 'job_city']]
    print(display.head())
