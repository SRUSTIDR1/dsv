import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_universities_in_India"
data = requests.get(url).text

soup = BeautifulSoup(data, 'html.parser')
table = soup.find('table', class_='wikitable sortable')

df = pd.DataFrame(columns = ['State', 'Central University', 'State University', 'Deemed', 'Private','Total'])

for row in table.tbody.find_all('tr'):
    columns = row.find_all('td')
    if(columns != []):
        col1 = columns[0].text.strip()
        col2 = columns[1].text.strip()
        col3 = columns[2].text.strip()
        col4 = columns[3].text.strip()
        col5 = columns[4].text.strip()
        col6 = columns[5].text.strip()
        df = df._append({'State':col1, 'Central University':col2, 'State University':col3, 'Deemed':col4, 'Private':col5,'Total':col6}, ignore_index=True)

print(df)