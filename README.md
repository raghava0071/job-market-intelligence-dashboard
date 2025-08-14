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

🧠 Architecture
flowchart TD
    A[Job Scraper] --> B[Cleaner & Preprocessor]
    B --> C[NLP Skill Extractor]
    C --> D[Clusterer (KMeans)]
    D --> E[Dashboard (Streamlit)]
    E --> F[User Filters & Charts]

🔧 Tech Stack

Python – Data processing, NLP, and backend logic

BeautifulSoup – Web scraping

Pandas / NumPy – Data cleaning and transformation

scikit-learn – Clustering (KMeans)

Matplotlib / WordCloud – Visualizations

Streamlit – Dashboard interface

🎓 Ideal For

Data Science Portfolio Projects

Skill Trend Monitoring

Job Market Research

Entry-level & OPT candidates seeking visibility

🙌 Future Enhancements

✅ Automate weekly refresh via GitHub Actions or cron

✅ Add resume matching using cosine similarity

✅ Enable login & saved filter options

✅ Public deployment via Streamlit Cloud

🧑‍💻 Author

Raghavendra Karanam
📍 Delray Beach, FL
📧 raghavendrakaranam30@gmail.com
🔗 LinkedIn | GitHub


---

## 📦 Want the Graphs & Images?

Once you're done rebuilding the dashboard locally:

1. Take screenshots of:
   - Skill frequency bar chart
   - Word cloud
   - Filtered job listings table
   - Cluster distribution chart

2. Save them as:
   - `skills_bar_chart.png`
   - `wordcloud.png`
   - `cluster_counts.png`
   - `dashboard_demo.png`

3. Use these in your LinkedIn post and also embed them in the `README.md` using:

```markdown
![Skill Chart](images/skills_bar_chart.png)
![Word Cloud](images/wordcloud.png)
