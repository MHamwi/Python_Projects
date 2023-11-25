from Translator import translate_arabic_to_english
from qr_code import generate_qr_code
import requests
from bs4 import BeautifulSoup
import csv
import urllib.parse
from PIL import Image
from io import BytesIO

row_snap_list=[]

def download_and_save_image(url, new_name, save_path="."):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open the image using Pillow
            image = Image.open(BytesIO(response.content)).convert('RGB')
            
            # Save the image with the provided new name and PNG format
            image.save(f"{save_path}/{new_name}.png", "PNG")
            
            print(f"Image '{new_name}' saved successfully.")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

def arabic_to_percent_encoding(arabic_url):
    # Parse the Arabic URL and encode it to the percentage encoding standard
    encoded_url = urllib.parse.quote(arabic_url, safe='/:?=&')

    return encoded_url


def remove_empty_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            # Check if the row is empty (all values are empty strings)
            if not all(cell == '' for cell in row):
                writer.writerow(row)

def main ():
    init_url= input(f'please write the url of website that you want to scrapping: ')
    n = input("please enter how many pages do you want to scrap? ")#https://crystalat.sa/products   try this to test the code
    qr_path= input("Enter the path, where you want to save product's Qr ")
    image_path= input("Enter the path, where you want to save product's image ") # for testing on my PC rf"E:\Desktop\Graphic Design\Crystalat\2023\11\22\Web Scrapping\Products_Images\{ids[0].replace('/','-')+'.png'}"
    csv_columns = ["NO","id","title","title_EN","description","description_EN","'@Image_Path","'@Qr_Code"]
    file_name=input('Enter the name of CSV file which you want to create')
    csv_container = input("Enter the path of the CSV File where the data will be stored")+f'/{file_name}.csv'
    # Specify the input and output csv file paths
    input_file = csv_container  # Replace with the path to your temp CSV file
    final_csv=input('What is the nane which you like to provide for the final csv file')
    output_file = input(f'What is the path which you like {final_csv} to be saved in')+f'/{final_csv}.csv'
    with open (csv_container,'w') as csvFile:
        #print(row_snap_list)
        dit_writer = csv.DictWriter(csvFile,csv_columns)
        dit_writer.writeheader()  
        for i in  range(1,int(n)+1):
            row_snap_dic={}
            #products_list = []
            print (f'now we are in the page {i}')
            url= f"{init_url}?page={i}"
            #url= f"https://crystalat.sa/products?page={i}&search=0"
            headers = {
            'Cookie': 'XSRF-TOKEN=eyJpdiI6Ik9jTGZDVVJTVWtlZDUyRXFFNjdzWHc9PSIsInZhbHVlIjoiTGNJMnJLZXUvM0pYRTBuKzNob2RVNjVudVZHYmRHV3ZIb2N3Wnh3QU4zOEFuZm82S3F4R1NDM2pXRXIvNXhJYTVtbEdUWHlRUEhvRnU3anI1S3NaVXFUUGdqY0dETzZuZ0l2RDd5T20xeVVzbnRiWGFEMG92dGFXT3dIdUJ4ZDQiLCJtYWMiOiJjN2IzOTVmOWJkZGI0MThjMjQ4YzExMTZkOWEwMGNlZDg1MDExMmVmOWRjYmQ1OWIzOWQ4M2JmYWZmNWQ3YTJhIiwidGFnIjoiIn0eyJpdiI6Imp2WlFkd0c0NE9JTS9sNWw0eWZRbUE9PSIsInZhbHVlIjoibGpoZm93dEhkd3RSMHdUd2VvbFV5d3FMZC9iUFZXTUNmY0xlbit2dCsvblBVQzM2eWtNRTI4WWVZa1dPTitwZ1VNVStzWFlJS0crOWFxbFVDYkl5TzRocWllOGxadExsUSt2RGNEd0Rtb1RaWENvWmsxNDdKdjVSd2hsdW9nVFIiLCJtYWMiOiIxZWEyODkyMjMxZjg5YjRmZTI4MTY3MWMwODM1YjA5YTg5OTRiYTQwNmIzMjBhMTg3YmU3MWEwMGU4MjZlOTE3IiwidGFnIjoiIn0%3D'
            }   
            
            page = requests.get(url,headers=headers)
            print(page.status_code)
            src = page.content
            soup = BeautifulSoup(src,"lxml")
            try:
                
                products=soup.find('div',{"class":"row products-list"}).find_all('div',{"class":"prod-col"})
                # get product information
                print(f'the number of products at page: {i} is {len(products)}')
                for item in range(len(products)):
                        row_snap_dic["NO"]=item+1
                    #try:
                        # get product name
                        try:
                            #print(products[item])
                            names = products[item].find('div',{"class":"product-title"}).text
                            
                            row_snap_dic["title"]=names
                            row_snap_dic["title_EN"]= translate_arabic_to_english(names)
                        except Exception as a:
                            print(f'error {a}')
                            continue
                        #ــــــــــــــــــــــــ
                        # get product links
                        try:
                            links = products[item].find('a')['href']
                            # Input your Arabic URL here
                            arabic_url = links
                            # Call the function to convert the Arabic URL to percentage encoding
                            encoded_url = arabic_to_percent_encoding(arabic_url)
                            
                            #print(arabic_url)
                            #print(encoded_url)
                            url= f'https://crystalat.sa{encoded_url}'
                            #print(url)
                            src = requests.get(url, headers)
                            soup = BeautifulSoup(src.content,"lxml")
                            try:
                                descrp = soup.find('div',{"class":"description-paragrah text-justify description-text-clear"}).text
                                descrp = descrp.replace('\n', ' ').replace('-', '.')
                                row_snap_dic['description'] = descrp
                                row_snap_dic['description_EN'] = translate_arabic_to_english(descrp)
                                #print(descrp)
                            except:
                                row_snap_dic['description'] = '-'
                                row_snap_dic['description_EN'] = '-'
                        except  Exception as m:
                            print(m)
                        #ــــــــــــــــــــــــ

                        # get product id and generate for each product an QR code image that linked with its ID
                        try:
                            ids = soup.find('div',{"class":"product-sku"}).text.split()
                            #print(ids)
                            row_snap_dic['id'] = ids[0].replace('/','-')
                            
                            generate_qr_code(url,ids[0].replace('/','-'),qr_path)
                        except Exception as c:
                            
                            print(f'error {ids[0]} {c}')
                            continue
                        #ــــــــــــــــــــــــ
                        # get product's image's link
                        try:
                            images = products[item].find('div',{"class":"content"}).find('img')['src']
                            
                            row_snap_dic["'@Image_Path"] = image_path +'/'+ids[0].replace('/','-')+'.png'
                            download_and_save_image(images,ids[0].replace('/','-'),image_path)
                        except:
                            print('error D')
                            continue

                        # write the path for each qr code in the row of each product
                        
                        row_snap_dic["'@Qr_Code"]= qr_path+'/'+ids[0].replace('/','-')+'.png'
                        # for each product write a line in a csv file
                        try:
                            dit_writer.writerow(row_snap_dic)
                        except Exception as e:        
                    #except Exception as e:
                            print(f'error {e}')
                            pass
            except Exception as q:
                print("error at the start point: "+q)
                continue

    # Call the function to remove empty lines
    remove_empty_lines(input_file, output_file)
main()

            
