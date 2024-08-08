import os
from urllib.parse import urljoin

from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://www.espncricinfo.com/cricketers/team/india-6'
response=requests.get(url)
soup=BeautifulSoup(response.text ,'html.parser')
#print(soup)
Player_Name=[name.text for name in soup.findAll('span',class_='ds-text-tight-l')]
Player_Age=[age.text for age in soup.findAll('span',class_='ds-text-tight-m ds-font-regular ds-text-typo-mid3')]

def download_image(url, folder_path, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(folder_path, file_name), 'wb') as file:
            file.write(response.content)

img_tags = soup.find_all('img')
folder_path = 'downloaded_images'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Loop through all image tags and download the images
for i, img in enumerate(img_tags):
    img_url = img.get('src')
    if img_url:
        # Convert relative URLs to absolute URLs
        img_url = urljoin(url, img_url)
        # Create a file name based on the index
        file_name = f'image_{i + 1}.jpg'
        # Download the image
        download_image(img_url, folder_path, file_name)
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')