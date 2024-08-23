import requests
from bs4 import BeautifulSoup
import csv

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
page_number = 1

with open('books.csv','w',newline='',encoding='utf-8') as csvfile:
    fieldnames = ['Title','Price']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)

    writer.writeheader()

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
            writer.writerow({'Title':title,'Price':price})

        page_number += 1
