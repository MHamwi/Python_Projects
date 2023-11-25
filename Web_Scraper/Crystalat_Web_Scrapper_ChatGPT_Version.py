from Translator import translate_arabic_to_english
from qr_code import generate_qr_code
import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import quote
from PIL import Image
from io import BytesIO


def download_and_save_image(url, new_name, save_path="."):
    """
    Download an image from the given URL and save it with the specified name.

    Parameters:
    - url: The URL of the image.
    - new_name: The desired name for the saved image.
    - save_path: The path where the image will be saved. Default is the current directory.
    """
    try:
        response = requests.get(url)

        if response.status_code == 200:
            image = Image.open(BytesIO(response.content)).convert('RGB')
            image.save(f"{save_path}/{new_name}.png", "PNG")

            print(f"Image '{new_name}' saved successfully.")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while downloading image: {e}")


def arabic_to_percent_encoding(arabic_url):
    """
    Convert Arabic URL to percent encoding.

    Parameters:
    - arabic_url: The Arabic URL to be encoded.

    Returns:
    - encoded_url: The percent-encoded URL.
    """
    try:
        encoded_url = quote(arabic_url, safe='/:?=&')
        return encoded_url
    except Exception as e:
        print(f"An error occurred while encoding the URL: {e}")
        return None


def scrape_product_info(product, qr_path, image_path, csv_writer):
    """
    Scrape product information, generate QR code, and save data to CSV.

    Parameters:
    - product: BeautifulSoup object representing the product.
    - qr_path: The path where QR codes will be saved.
    - image_path: The path where product images will be saved.
    - csv_writer: CSV writer object for writing data.
    """
    row_snap_dic = {}

    try:
        names = product.find('div', {"class": "product-title"}).text
        row_snap_dic["title"] = names
        row_snap_dic["title_EN"] = translate_arabic_to_english(names)

        links = product.find('a')['href']
        arabic_url = links
        encoded_url = arabic_to_percent_encoding(arabic_url)

        if encoded_url:
            url = f'https://crystalat.sa{encoded_url}'
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "lxml")

            try:
                descrp = soup.find('div', {"class": "description-paragrah text-justify description-text-clear"}).text
                descrp = descrp.replace('\n', ' ').replace('-', '.')
                row_snap_dic['description'] = descrp
                row_snap_dic['description_EN'] = translate_arabic_to_english(descrp)
            except Exception as e:
                print(f"An error occurred while getting product description: {e}")
                row_snap_dic['description'] = '-'
                row_snap_dic['description_EN'] = '-'

            try:
                ids = soup.find('div', {"class": "product-sku"}).text.split()
                row_snap_dic['id'] = ids[0].replace('/', '-')
                generate_qr_code(url, ids[0].replace('/', '-'), qr_path)
            except Exception as e:
                print(f"An error occurred while getting product ID or generating QR code: {e}")
                return

            try:
                images = product.find('div', {"class": "content"}).find('img')['src']
                row_snap_dic["@Image_Path"] = f"{image_path}/{ids[0].replace('/', '-')}.png"
                download_and_save_image(images, ids[0].replace('/', '-'), image_path)
            except Exception as e:
                print(f"An error occurred while downloading image: {e}")
                return

            row_snap_dic["@Qr_Code"] = f"{qr_path}/{ids[0].replace('/', '-')}.png"

            try:
                csv_writer.writerow(row_snap_dic)
            except Exception as e:
                print(f"An error occurred while writing to CSV: {e}")
    except Exception as e:
        print(f"An error occurred while processing product info: {e}")


def scrape_and_save_data(init_url, n, qr_path, image_path, csv_container):
    """
    Scrape data from the website, generate QR codes, and save data to CSV.

    Parameters:
    - init_url: The base URL of the website.
    - n: The number of pages to scrape.
    - qr_path: The path where QR codes will be saved.
    - image_path: The path where product images will be saved.
    - csv_container: The path to the CSV file where data will be stored.
    """
    csv_columns = ["NO", "id", "title", "title_EN", "description", "description_EN", '@Image_Path', '@Qr_Code']

    with open(csv_container, 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, csv_columns)
        csv_writer.writeheader()

        for i in range(1, int(n) + 1):
            print(f'Now scraping page {i}')

            url = f"{init_url}?page={i}"
            headers = {'Cookie': 'your_cookie_here'}  # Add your cookie value

            try:
                page = requests.get(url, headers=headers)
                print(page.status_code)
                src = page.content
                soup = BeautifulSoup(src, "lxml")

                products = soup.find('div', {"class": "row products-list"}).find_all('div', {"class": "prod-col"})
                print(f'The number of products on page {i} is {len(products)}')

                for item, product in enumerate(products, start=1):
                    row_snap_dic = {"NO": item}
                    scrape_product_info(product, qr_path, image_path, csv_writer)
            except Exception as e:
                print(f"An error occurred while scraping data: {e}")


def remove_empty_lines(input_file, output_file):
    """
    Remove empty lines from a CSV file.

    Parameters:
    - input_file: The path to the input CSV file.
    - output_file: The path to the output CSV file without empty lines.
    """
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            for row in reader:
                if not all(cell == '' for cell in row):
                    writer.writerow(row)
    except Exception as e:
        print(f"An error occurred while removing empty lines: {e}")


def main():
    init_url = input('Please enter the URL of the website that you want to scrape: ')
    n = input("Please enter how many pages you want to scrape: ")
    qr_path = input("Enter the path where you want to save product QR codes: ")
    image_path = input("Enter the path where you want to save product images: ")
    file_name = input('Enter the name of the CSV file you want to create: ')
    csv_container = input("Enter the path of the CSV file where the data will be stored") + f'/{file_name}.csv'
    input_file = csv_container
    final_csv = input('What is the name you would like to provide for the final CSV file: ')
    output_file = input(f'What is the path where you would like {final_csv} to be saved') + f'/{final_csv}.csv'

    scrape_and_save_data(init_url, n, qr_path, image_path, csv_container)
    remove_empty_lines(input_file, output_file)


if __name__ == "__main__":
    main()
