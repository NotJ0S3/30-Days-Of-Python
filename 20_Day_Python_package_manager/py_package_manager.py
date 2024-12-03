# Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
# the min, max, mean, median, standard deviation of cats' weight in metric units.
# the min, max, mean, median, standard deviation of cats' lifespan in years.
# Create a frequency table of country and breed of cats
# Read the countries API and find
# the 10 largest countries
# the 10 most spoken languages
# the total number of languages in the countries API
# UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4

# All the site webs are 404, just the exercises 2 its available so lets do it:

import requests
from statistics import mean, median, stdev

cats_api = 'https://api.thecatapi.com/v1/breeds'

response = requests.get(cats_api)
# print(response)
# print(response.status_code)
# print(response.headers)
# print(response.text)

cats = response.json()

cats_weight = [dct.get("weight") for dct in cats]
cats_weight_metric = [int(dct.get("metric")[0]) for dct in cats_weight]
min_of_cats_weight = min(cats_weight_metric)
max_of_cats_weight = max(cats_weight_metric)
mean_of_cats_weight = mean(cats_weight_metric)
median_of_cats_weight = median(cats_weight_metric)
stdev_of_cats_wight = stdev(cats_weight_metric)
print(stdev_of_cats_wight)