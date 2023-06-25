# Referenced sources:
# https://pypi.org/project/tqdm/2.2.3/ (since progress.bar library did not work with Jupyter Notebook)
# https://apipheny.io/free-api/#apis-without-key
# https://www.geeksforgeeks.org/python-web-scraping-tutorial/

import requests
from bs4 import BeautifulSoup
import urllib
import os
from tqdm import tqdm


def access_website(website_url):
    try:
        response = requests.get(website_url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as exception:
        print(f"Error accessing the website: {exception}")
        return None


def scrape_images(website_url, quantity_of_images_to_download, directory_name):
    content = access_website(website_url)
    if not content:
        return

    soup = BeautifulSoup(content, "html.parser")
    image_elements = soup.find_all("img")
    quantity = 0
    directory = directory_name
    os.makedirs(directory, exist_ok=True)

    with tqdm(total=quantity_of_images_to_download) as pbar:
        for image in image_elements:
            image_url = image["src"]

            try:
                urllib.request.urlretrieve(image_url, f"{directory}/image_{quantity}.jpg")
                quantity += 1
                pbar.update(1)

                if quantity == quantity_of_images_to_download:
                    break

            except urllib.error.HTTPError as exception:
                print(f"Error downloading image: {exception}")
            except urllib.error.URLError as exception:
                print(f"Error accessing the image URL: {exception}")
            except OSError as exception:
                print(f"Error upon saving: {exception}")


if __name__ == "__main__":
    url = "https://unsplash.com/s/photos/cat"
    num_images = 10
    scrape_images(url, num_images, "img")
