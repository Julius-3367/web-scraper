import requests
from bs4 import BeautifulSoup
import csv
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Set up logging
logging.basicConfig(filename='scraping.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_website(url):
    try:
        # Send a GET request to the website
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the title of the website
        title = soup.title.string.strip() if soup.title else 'No title found'

        # Extract all links on the website
        links = [link.get('href') for link in soup.find_all('a', href=True)]

        logging.info(f'Successfully scraped {url}')
        return url, title, links

    except requests.exceptions.RequestException as e:
        logging.error(f"Error accessing {url}: {e}")
        return url, 'Error', []

def save_to_csv(data, filename='scraped_data.csv'):
    # Save the scraped data to a CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)

def main():
    # List of websites to scrape
    websites = [
        'https://example.com',
        'https://example2.com',
        # Add more websites here
    ]

    # Prepare the CSV file with headers
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Website', 'Title', 'Links'])

    # Use ThreadPoolExecutor for parallel processing
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(scrape_website, website) for website in websites}

        for future in as_completed(futures):
            result = future.result()
            save_to_csv([result])

            # Optionally add a small delay to avoid overwhelming servers
            time.sleep(0.1)

    logging.info("Scraping complete and data saved to 'scraped_data.csv'")

if __name__ == '__main__':
    main()

