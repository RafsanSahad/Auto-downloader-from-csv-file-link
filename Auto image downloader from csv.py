import os
import csv
import requests
from urllib.parse import urlparse

def download_thumbnails(csv_path, save_directory):
    # Ensure the save directory exists
    os.makedirs(save_directory, exist_ok=True)
    
    # Read CSV file
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            image_url = row.get("Images")
            if image_url:
                try:
                    response = requests.get(image_url, stream=True)
                    response.raise_for_status()
                    
                    # Extract file name from URL
                    parsed_url = urlparse(image_url)
                    filename = os.path.basename(parsed_url.path)
                    save_path = os.path.join(save_directory, filename)
                    
                    # Save the image
                    with open(save_path, 'wb') as img_file:
                        for chunk in response.iter_content(1024):
                            img_file.write(chunk)
                    print(f"Downloaded: {filename}")
                except requests.RequestException as e:
                    print(f"Failed to download {image_url}: {e}")

# Define file paths
csv_file_path = r"D:\Work\Liam\NCRP pub and video structure (1)\NCRP pub and video structure\publications\CSVs"
save_directory = r"D:\Work\Liam\NCRP pub and video structure (1)\NCRP pub and video structure\publications\data\thumbnails\commentaries"

# Run the function
download_thumbnails(csv_file_path, save_directory)
