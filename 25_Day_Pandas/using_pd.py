# Read the hacker_news.csv file from data directory
import pandas as pd

df = pd.read_csv('C:/Users/alexm/OneDrive/Desktop/Jose Manuel/Programacion/30-Days-Of-Python/data/hacker_news.csv')
print(df)
print('----------------------')

# Get the first five rows
print(df.head())
print('----------------------')


# Get the last five rows
print(df.tail())
print('----------------------')


# Get the title column as pandas series
title = df['title']
print(title)
print('----------------------')


# Count the number of rows and columns
print(df.shape)
print('----------------------')


# Filter the titles which contain python
py_titles = df[df['title'] == 'python']
print(py_titles)
print('----------------------')

# Filter the titles which contain JavaScript
js_titles = df[df['title'] == 'javascript']
print(js_titles)

# Explore the data and make sense of it