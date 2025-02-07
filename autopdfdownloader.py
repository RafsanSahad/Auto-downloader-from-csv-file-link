import os
import csv
import requests
from urllib.parse import urlparse

def download_pdfs(csv_path, save_directory):
    # Ensure the save directory exists
    os.makedirs(save_directory, exist_ok=True)
    
    # Read CSV file
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pdf_url = row.get("Download 1 URL")
            if pdf_url:
                try:
                    response = requests.get(pdf_url, stream=True)
                    response.raise_for_status()
                    
                    # Extract file name from URL
                    parsed_url = urlparse(pdf_url)
                    filename = os.path.basename(parsed_url.path)
                    save_path = os.path.join(save_directory, filename)
                    
                    # Save the PDF
                    with open(save_path, 'wb') as pdf_file:
                        for chunk in response.iter_content(1024):
                            pdf_file.write(chunk)
                    print(f"Downloaded: {filename}")
                except requests.RequestException as e:
                    print(f"Failed to download {pdf_url}: {e}")

# Define file paths
csv_file_path = r"D:\Work\Liam\NCRP pub and video structure (1)\NCRP pub and video structure\publications\CSVs\Commentaries.csv"
pdfs_directory = r"D:\Work\Liam\NCRP pub and video structure (1)\NCRP pub and video structure\publications\data\Publications"

# Run the function
download_pdfs(csv_file_path, pdfs_directory)
