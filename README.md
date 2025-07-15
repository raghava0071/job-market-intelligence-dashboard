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
# Clone the repository
git clone https://github.com/your-username/job-intel-dashboard.git
cd job-intel-dashboard

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Streamlit dashboard
streamlit run app.py
