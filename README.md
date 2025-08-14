# 📊 Job Market Intelligence Dashboard

An intelligent, real-time dashboard that scrapes job listings, extracts trending skills, clusters similar roles, and visualizes insights using **Python**, **NLP**, and **Streamlit**.

---

## ✨ Key Features

- 🕵️ **Real-Time Job Scraping** – Extract listings from job sites using `requests`, `BeautifulSoup`, and `pandas`.
- 🧠 **NLP Skill Extraction** – Uses `regex`, `tokenization`, and keyword matching to extract trending skills from job descriptions.
- 📊 **Interactive Dashboard** – Built using `Streamlit` to visualize job trends, skill clouds, and role clusters.
- 🧩 **Job Clustering** – Groups roles using `TfidfVectorizer` and `KMeans` for industry-level grouping.
- 🔍 **Role & Skill Filters** – Enables filtering by location, skill keywords, and job clusters.
- 🔄 **Auto-Refresh Ready** – Designed to support weekly automation via GitHub Actions or cron jobs.

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/raghava0071/job-market-intelligence-dashboard.git
cd job-market-intelligence-dashboard

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate         # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Launch the Streamlit dashboard
streamlit run app.py
# 💬 Sample Outputs
## 📂 Files Generated
