import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL
BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

# List to store product data
products = []

# Scrape first 5 pages
for page_num in range(1, 6):
    url = BASE_URL.format(page_num)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Select all product pods
    items = soup.select("article.product_pod")

    for item in items:
        name = item.h3.a['title']
        price = item.select_one(".price_color").text.strip()
        rating = item.p['class'][1]  # E.g., 'One', 'Two', etc.

        products.append({
            "Name": name,
            "Price": price,
            "Rating": rating
        })

# Convert to DataFrame
df = pd.DataFrame(products)

# Save to CSV
df.to_csv("products.csv", index=False)

print("Scraping complete. Data saved to 'products.csv'.")