# 📊 Job Market Intelligence Dashboard

An intelligent, real-time dashboard that scrapes job listings, extracts trending skills, clusters similar roles, and visualizes insights using Python, NLP, and Streamlit.

---

## ✨ Key Features

- 🕵️ **Real-Time Job Scraping** – Extract listings from job sites using `requests`, `BeautifulSoup`, and `pandas`.
- 🧠 **NLP Skill Extraction** – Uses regex, tokenization, and keyword matching to extract trending skills from descriptions.
- 📊 **Interactive Dashboard** – Built using `Streamlit` to visualize job trends, skill clouds, and clusters.
- 🧩 **Job Clustering** – Uses `TfidfVectorizer` + `KMeans` to group similar job roles based on cleaned descriptions.
- 🔍 **Role & Skill Filters** – Allows users to filter jobs by cluster, city, or skill.
- 🔄 **Auto-Refresh Ready** – Supports future automation via GitHub Actions or cron.

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/raghava0071/job-market-intelligence-dashboard.git
cd job-market-intelligence-dashboard

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Streamlit dashboard
streamlit run app.py

💬 Sample Outputs
📂 Files Generated:

raw_jobs.csv

cleaned_jobs.csv

clustered_jobs.csv

🎯 NLP Output:

Extracted top 50 trending skills

Mapped job roles to clusters

Word clouds and bar charts for skill demand

📈 Dashboard Filters:

Job Cluster

Location

Keyword (Skill)
