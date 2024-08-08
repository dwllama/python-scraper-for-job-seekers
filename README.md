# Job Scraper

Influenced by a close friend who was laid off from her job earlier this year, this script is designed to scrape job listings from the careers pages of desired companies and search for specific job keywords. The results are then saved to a CSV file showing the user which copmanies have roles the user is looking for. This script can be scheduled to run automatically on a daily basis to save the user an immense amount of time vs visiting each individual URL separatelty to check for updated roles.

## Features

- Scrapes job listings from multiple company careers pages.
- Searches for specific job keywords in the scraped data.
- Saves the results to a CSV file with a timestamp in the filename.

## Requirements

- Python 3.x
- requests
- beautifulsoup4
- csv
- datetime

You can install the required Python packages using pip:

```bash
pip install requests beautifulsoup4
Usage
Update the companies_careers list with the URLs of the companies' careers pages you'd like to scrape.

companies_careers = [
    "https://example.com/careers/",
    "https://example2.com/careers/",
]
Update the job_keywords list with the keywords of the roles you are searching for.

job_keywords = ["customer success manager", "product marketing", "director customer success"]
Run the script. The results will be saved to a CSV file named job_results_YYYY-MM-DD_HH-MM-SS.csv.
Functions
scrape_webpage(url, keywords)
Scrapes an entire webpage and checks for keyword matches.

url: The URL of the webpage to scrape.
keywords: A list of keywords to search for in the webpage.
Returns a dictionary with the matched keywords and the total number of keywords found.

save_results_to_csv(results)
Saves the results to a CSV file with a timestamp in the filename.

results: A dictionary of results where the keys are the company URLs and the values are the job data.
