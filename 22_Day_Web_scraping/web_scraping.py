# Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').

import requests
import json
from bs4 import BeautifulSoup

def excercise1():
    url = 'http://www.bu.edu/president/boston-university-facts-stats/'

    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    data = {
        'title': soup.title.string,
        'body': soup.body.string,
        'status_code': response.status_code
    }

    with open('./22_Day_Web_scraping/bu.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

# Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file

def excercise2():
    url = 'https://archive.ics.uci.edu/ml/datasets.php'

    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    print(response.status_code) # STATUS CODE 404 

# Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

data = {
    'table': soup.table.string
}

with open('./22_Day_Web_scraping/USA_presidents.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)