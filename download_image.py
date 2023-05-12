import os
import requests


def download_image(image_url: str) -> str:
    response = requests.get(image_url)

    if response.status_code != 200:
        raise Exception(f"Failed to download image from URL: {image_url}")
    
    filename = os.path.basename(image_url)
    filepath = f"data/train/{filename}.jpg"
    
    with open(filepath, 'wb') as f:
        f.write(response.content)
    
    return filepath


if __name__ == "__main__":
    image_url = "https://media.cnn.com/api/v1/images/stellar/prod/220715122428-macbook-air-m2-review-9.jpg?c=16x9&q=h_270,w_480,c_fill/f_webp"
    image_path = download_image(image_url)
    
    print(image_path)
