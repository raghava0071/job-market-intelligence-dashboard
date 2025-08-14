import http.client
import json
import pandas as pd

def fetch_job_data(role="data analyst", pages=1):
    conn = http.client.HTTPSConnection("jsearch.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "3fbaa47488msh660a07cdf52b73ap143978jsn9af97fac883b",
        'X-RapidAPI-Host': "jsearch.p.rapidapi.com"
    }

    all_jobs = []

    for page in range(1, pages + 1):
        conn.request("GET", f"/search?query={role.replace(' ', '%20')}&page={page}&num_pages=1&country=us&date_posted=month", headers=headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        job_results = json.loads(data).get('data', [])
        all_jobs.extend(job_results)

    return pd.DataFrame(all_jobs)

# Run it and save the results
df = fetch_job_data("data analyst", 2)
df.to_csv("raw_jobs.csv", index=False)
print("✅ Job data saved to raw_jobs.csv")


