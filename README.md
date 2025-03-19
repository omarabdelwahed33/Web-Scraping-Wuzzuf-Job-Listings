# Web-Scraping-Wuzzuf-Job-Listings
Overview

This Python script scrapes job listings for the keyword "Illustrator" from Wuzzuf and extracts key job details such as:

Job Title

Company Name

Job Type

The extracted data is then saved into a CSV file for further analysis.

Requirements

Ensure you have the following installed before running the script:

Python 3.x

Required Python Libraries:

beautifulsoup4

urllib

csv

You can install the required libraries using:

pip install beautifulsoup4

How It Works

The script sends an HTTP request to Wuzzuf’s job search page for "Illustrator" positions.

It parses the HTML content using BeautifulSoup.

It extracts job titles, company names, and job types from the relevant HTML elements.

The extracted data is written into a CSV file (wuzzuf.csv).

Usage

Download the script and ensure you have Python installed.

Run the script using the command:

python script.py

Find the CSV output at the specified location in the script (C:/Users/DELL/Documents/web scrapinggg/wuzzuf.csv).

Notes

The script assumes a specific HTML structure, which may change over time. If the website updates its structure, selectors might need to be updated.

Ensure you comply with Wuzzuf's terms of service when scraping data.

Future Improvements

Implement error handling for missing or changed elements.

Convert the script into a function-based or object-oriented structure for better reusability.

Add support for multiple search queries dynamically.
