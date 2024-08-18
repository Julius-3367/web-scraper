# Web Scraper

## Overview

This project is a Python-based web scraper that extracts the title and all links from a list of websites. The script runs concurrently across multiple websites to improve performance and saves the scraped data into a CSV file.

## Files

- `scraper.py`: The main script that performs the web scraping.
- `scraping.log`: A log file that records the success or failure of scraping each website.
- `scraped_data.csv`: The CSV file where the scraped data is stored.
- `.gitignore`: A file to exclude unnecessary files from being pushed to GitHub.

## How to Use

1. Clone this repository to your local machine.
2. Install the required Python libraries:
   ```bash
   pip install requests beautifulsoup4
