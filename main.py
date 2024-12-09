import requests
from requests.exceptions import HTTPError
import csv

# List of URLs to check
URLs = [
    'https://www.google.com/',
    'https://www.amazon.com/invalid',
    'https://www.mscdirect.com/',
    'https://www.amazon.com/',
    'https://www.mscdirect.com/browse/Holemaking?navid=2106067'
]

# CSV file name
output_file = "url_results.csv"

# Open the CSV file for writing
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['URL', 'Status Code', 'Result'])

    # Process each URL
    for url in URLs:
        try:
            # Send GET request
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        except HTTPError as http_err:
            print(f"HTTP error occurred for {url}: {http_err}")
            writer.writerow([url, response.status_code if 'response' in locals() else 'N/A', f"HTTP Error: {http_err}"])
        except Exception as err:
            print(f"Other error occurred for {url}: {err}")
            writer.writerow([url, 'N/A', f"Other Error: {err}"])
        else:
            print(f"Success for {url}")
            writer.writerow([url, response.status_code, "Success"])
