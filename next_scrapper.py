
"""Handling pages with the Next button"""
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html'

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    footer_element = soup.find('li',class_='current')
    #footer_element = soup.select_one('li.current')
    print(footer_element.text.strip())
    # Do more with each page.

    # Find the next page to scrape in the pagination.
    next_page_element = soup.select_one('li.next a')
    if next_page_element:        
        next_page_url = next_page_element['href']
        url = urljoin(url, next_page_url)
        print(url)
    else:
        break