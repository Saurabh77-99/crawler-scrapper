import requests
from bs4 import BeautifulSoup
import json

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
page_number = 1

books_data = []

while True:
    url = base_url.format(page_number)
    print(f"Scraping URL: {url}")

    response = requests.get(url)

    if response.status_code != 200:
        print("No more pages to scrape. Exiting.")
        break

    soup = BeautifulSoup(response.text,'html.parser')

    books = soup.find_all('article',class_='product_pod')

    if not books:
        print("No more books found on this page. Exiting.")
        break

    for book in books:
        title = book.h3.a['title']
        price = book.find('p',class_='price_color').text
        books_data.append({'Title':title,'Price':price})

    page_number += 1

with open('books.json','w',encoding='utf-8') as jsonfile:
    json.dump(books_data,jsonfile,indent=4)

print("Data has been successfully written to books.json")