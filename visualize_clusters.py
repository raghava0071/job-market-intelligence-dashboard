import pandas as pd
import matplotlib.pyplot as plt

# Load your clustered data
df = pd.read_csv("cleaned_jobs.csv")

# Use 'cluster' column (make sure it exists)
if 'cluster' not in df.columns:
    print("❌ Error: 'cluster' column not found. Run cluster_roles.py first.")
    exit()

# Plot job count per cluster
cluster_counts = df['cluster'].value_counts().sort_index()

plt.figure(figsize=(8, 4))
cluster_counts.plot(kind='bar', color='skyblue')
plt.title("Job Count per Cluster")
plt.xlabel("Cluster Number")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("cluster_counts.png")
plt.show()
