# Exercises: Level 1
# Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words

def counting_lines(direction):
    import re
    re_patt = r'[a-zA-Z]'
    with open(direction) as f:
        txt = f.read()
        lines = len(txt.splitlines())
        words = len(re.findall(re_patt, txt))
        return f'The speech has {lines} lines and {words} words'
        
print(counting_lines('./data/obama_speech.txt'))
print(counting_lines('./data/michelle_obama_speech.txt'))
print(counting_lines('./data/donald_speech.txt'))
print(counting_lines('./data/melina_trump_speech.txt'))

# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

def most_spoken_lans(filename = str, top = int):
    import json
    import re
    with open(filename) as f:
        txt = f.read()
        countries_list = json.loads(txt)
        total_lans = set([dct.get("languages")[0] for dct in countries_list])
        list_lans_by_country = [tuple([len(re.findall(language, txt)), language]) for language in total_lans]
        list_lans_by_country.sort(reverse=True)
        return list_lans_by_country[:top]

print(most_spoken_lans('./data/countries_data.json', 10))
print(most_spoken_lans('./data/countries_data.json', 3))

# # Your output should look like this
# print(most_spoken_languages(filename='./data/countries_data.json', 10))
# [(91, 'English'),
# (45, 'French'),
# (25, 'Arabic'),
# (24, 'Spanish'),
# (9, 'Russian'),
# (9, 'Portuguese'),
# (8, 'Dutch'),
# (7, 'German'),
# (5, 'Chinese'),
# (4, 'Swahili'),
# (4, 'Serbian')]

# # Your output should look like this
# print(most_spoken_languages(filename='./data/countries_data.json', 3))
# [(91, 'English'),
# (45, 'French'),
# (25, 'Arabic')]


# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

def most_populated_countries(filename, top):
    import json
    with open(filename) as f:
        txt = f.read()
        countries_list = json.loads(txt)
        list_of_names = [{'country':dct.get("name"), 'population':dct.get("population")} for dct in countries_list]
        list_of_names.sort(key=lambda dct: dct["population"], reverse=True)
        return list_of_names[:top]
        

print(most_populated_countries('./data/countries_data.json', 10))
print(most_populated_countries('./data/countries_data.json', 3))

# # Your output should look like this
# print(most_populated_countries(filename='./data/countries_data.json', 10))

# [
# {'country': 'China', 'population': 1377422166},
# {'country': 'India', 'population': 1295210000},
# {'country': 'United States of America', 'population': 323947000},
# {'country': 'Indonesia', 'population': 258705000},
# {'country': 'Brazil', 'population': 206135893},
# {'country': 'Pakistan', 'population': 194125062},
# {'country': 'Nigeria', 'population': 186988000},
# {'country': 'Bangladesh', 'population': 161006790},
# {'country': 'Russian Federation', 'population': 146599183},
# {'country': 'Japan', 'population': 126960000}
# ]

# # Your output should look like this

# print(most_populated_countries(filename='./data/countries_data.json', 3))
# [
# {'country': 'China', 'population': 1377422166},
# {'country': 'India', 'population': 1295210000},
# {'country': 'United States of America', 'population': 323947000}
# ]


# Exercises: Level 2
# Extract all incoming email addresses as a list from the email_exchange_big.txt file.

# import re
# re_patt = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
# with open('./data/email_exchanges_big.txt') as f:
#     txt = f.read()
#     emails = re.findall(re_patt, txt)
#     print(emails)
    

# Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output

def find_most_common_words(file, top):
    import re
    with open(file) as f:
        txt = f.read()
        # txt = re.sub('(\$|#|%|&|@)', '', txt)
        words_list = set(txt.split())
        matches = [tuple([len(re.findall(words, txt)), words]) for words in words_list]
        matches.sort(reverse=True)
        return matches[:top]

#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 10))
#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and'),
#     (4, 'a'),
#     (4, 'in'),
#     (3, 'that'),
#     (2, 'have'),
#     (2, 'I')]

#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 5))

#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and')]

# Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech

print(find_most_common_words('./data/obama_speech.txt', 10))
# print(find_most_common_words('./data/michelle_obama_speech.txt', 10))
print(find_most_common_words('./data/donald_speech.txt', 10))
print(find_most_common_words('./data/melina_trump_speech.txt', 10))

# Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory
# Find the 10 most repeated words in the romeo_and_juliet.txt

# print(find_most_common_words('./data/romeo_and_juliet.txt', 10))

# Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript

