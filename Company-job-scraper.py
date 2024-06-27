import requests
from bs4 import BeautifulSoup
import re
import csv
from datetime import datetime

# Original company /careers/ page of companies you'd like to work for below
companies_careers = [
    "https://example.com/careers/",
    "https://example2.com/careers/",

]

# Keywords for the role you are searching for at companies listed above. Account for different variations of roles to obtain more matches (eg: ML engineer, machine learning engineer) to enhance scraping accuracy
job_keywords = ["ml engineer", "machine learning engineer"]

def scrape_webpage(url, keywords):
    """Scrapes an entire webpage and checks for keyword matches."""
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        # Get all text content from the page (including HTML and CSS)
        page_text = soup.get_text(separator=" ") 

        matched_keywords = set()
        total_keywords_found = 0
        for keyword in keywords:
            if re.search(keyword, page_text, re.IGNORECASE):
                matched_keywords.add(keyword)
                total_keywords_found += 1

        return {"matched_keywords": matched_keywords, "total_keywords_found": total_keywords_found}

    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return None  # Return None for errors

# Loop through each company and scrape its webpage
results = {}
for company_url in companies:
    job_data = scrape_webpage(company_url, keywords)
    if job_data and job_data["total_keywords_found"] > 0:  # Only include if keywords found
        results[company_url] = job_data

# Function to save results to a CSV file
def save_results_to_csv(results):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"job_results_{timestamp}.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Company URL", "Matched Keywords", "Total Keywords Found"])
        for url, job_data in results.items():
            matched_keywords = ", ".join(job_data["matched_keywords"])
            total_keywords_found = job_data["total_keywords_found"]
            writer.writerow([url, matched_keywords, total_keywords_found])        

# Save the results to a CSV file
save_results_to_csv(results)
