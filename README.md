# 📊 Job Market Intelligence Dashboard #
An intelligent, real-time dashboard that scrapes job listings, extracts trending skills, clusters similar roles, and visualizes insights using Python, NLP, and Streamlit.

# ✨ Key Features # 
🕵️ Real-Time Job Scraping – Extracts listings from top job platforms using requests, BeautifulSoup, and pandas.

🧠 NLP Skill Extraction – Automatically identifies trending job skills using tokenization, regex, and keyword parsing.

📊 Interactive Dashboard – Built with Streamlit to visualize jobs, locations, skills, and clusters.

🧩 Job Clustering – Groups similar roles using TfidfVectorizer + KMeans for industry-level insights.

🔍 Role & Skill Filters – Users can filter data by location, cluster, and skill demand.

🔄 Auto Refresh Capability – Design supports weekly data refresh and future automation.

# 🚀 Quick Start #
bash
Copy
Edit
Clone the repository
git clone https://github.com/your-username/job-intel-dashboard.git
cd job-intel-dashboard

Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Launch Streamlit dashboard
streamlit run app.py


# 💬 Sample Outputs #
diff
Copy
Edit
📂 Files Generated:
- raw_jobs.csv
- cleaned_jobs.csv
- clustered_jobs.csv

# 🎯 NLP Output:
- Extracted top 50 trending skills
- Mapped job roles to clusters
- Word clouds and bar charts for skills in demand

# 📈 Dashboard Filters:
- Location
- Skill keyword
- Cluster group
🧠 Architecture
mermaid
Copy
Edit
flowchart TD
    A[Job Scraper] --> B[Cleaner & Preprocessor]
    B --> C[NLP Skill Extractor]
    C --> D[Clusterer (KMeans)]
    D --> E[Dashboard (Streamlit)]
    E --> F[User Filters & Charts]
🔧 Tech Stack
Python – Data processing, NLP

BeautifulSoup – Web scraping

Pandas / NumPy – Data wrangling

scikit-learn – Clustering (KMeans)

Streamlit – Dashboard visualization

Matplotlib / WordCloud – Skill cloud and charts

# 🎓 Ideal For
Data Science Portfolio Projects

Skill trend monitoring

Job market research

Entry-level and OPT candidates seeking visibility

🙌 Future Enhancements
✅ Automate weekly refresh via GitHub Actions or CRON

✅ Add resume matching using cosine similarity

✅ Add login module for saved filters

✅ Deploy public version via Streamlit Cloud

# 🧑‍💻 Author
Raghavendra Karanam
📍 Delray Beach, FL
📧 raghavendrakaranam30@gmail.com
🔗 LinkedIn | GitHub


