import requests
from bs4 import BeautifulSoup


def get_amazon_reviews(product_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    reviews = []
    for review in soup.find_all("span", class_="a-size-base review-text review-text-content"):
        reviews.append(review.get_text(strip=True))

    return reviews