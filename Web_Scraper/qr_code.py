import qrcode
import os

def generate_qr_code(url, unique_name, qr_path):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Specify the directory path
    save_path = qr_path #"E:/Desktop/Graphic Design/Crystalat/2023/11/22/Web Scrapping/QR CODE Images/"
    
    # Create the directory if it doesn't exist
    os.makedirs(save_path, exist_ok=True)
    
    # Construct the unique filename based on the ID number
    filename = f"{unique_name}.png"
    
    # Save the image
    img.save(os.path.join(save_path, filename))

if __name__ == "__main__":
    # Example usage with multiple URLs and unique names
    product_urls = [
        ("https://example.com/product1", "12345"),
        ("https://example.com/product2", "67890"),
        # Add more pairs as needed
    ]
    
    for url, unique_name in product_urls:
        generate_qr_code(url, unique_name)
        print(f"QR code for {url} with unique name {unique_name} generated successfully.")