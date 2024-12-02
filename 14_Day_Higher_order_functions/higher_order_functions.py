countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Exercises: Level 1
# Explain the difference between map, filter, and reduce.
# With map we can iterate over a list, set or tuple like we did with the "for" loop. With filter we can find especific
# data that we want to find in a list of data. And reduce is use to, for example, find the total of a list of numbers


# Explain the difference between higher order function, closure and decorator
# Higher order functions can accept other functions and return a function, closure is when you have a function inside another 
# function and it helps when you want to work whit modules and you don't want to export everythin. And decorator is
# for extend the behavior of another function

# Define a call function before map, filter or reduce, see examples.
# Use for loop to print each country in the countries list.
# Use for to print each name in the names list.
# Use for to print each number in the numbers list.

def printing_data(data):
    for i in data:
        print(i)

printing_data(countries)
printing_data(names)
printing_data(numbers)   

# Exercises: Level 2
# Use map to create a new list by changing each country to uppercase in the countries list

country_upper = list(map(lambda country : country.upper(), countries))
print(country_upper)

# Use map to create a new list by changing each number to its square in the numbers list

number_square = list(map(lambda number: number ** 2, numbers))
print(number_square)

# Use map to change each name to uppercase in the names list

name_upper = list(map(lambda name : name.upper(), names))
print(name_upper)

# Use filter to filter out countries containing 'land'.

def land_in_countries(country):
    if "land" in country:
        return True
    return False

land_countries = list(filter(land_in_countries, countries))
print(land_countries)

# Use filter to filter out countries having exactly six characters.

def country_len_char(country):
    if len(country) == 6:
        return True
    return False

country_len_six = list(filter(country_len_char, countries))
print(country_len_six)

# Use filter to filter out countries containing six letters and more in the country list.

def country_len_more_char(country):
    if len(country) >= 6:
        return True
    return False

country_len_more_six = list(filter(country_len_more_char, countries))
print(country_len_more_six)

# Use filter to filter out countries starting with an 'E'

def countries_starts_E(country):
    if country.startswith("E"):
        return True
    return False

countries_startswith_e = list(filter(countries_starts_E, countries))
print(countries_startswith_e)

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

def get_string_lists(lst):
    new_list = [str(i) for i in lst]        
    return new_list

print(get_string_lists(numbers))

# Use reduce to sum all the numbers in the numbers list.

from functools import reduce

sum_all_nums = reduce(lambda x, y: x + y, numbers)
print(sum_all_nums)

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

sentence = reduce(lambda x, y: x + ", " + y, countries)
print(sentence)

# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

from countries import countries

def categorize_countries():
    def common_pattern(country):
        if country.endswith('land') or country.endswith('ia') or country.endswith('island') or country.endswith('stan'):
            return True
        return False

    countries_ends_with = list(filter(common_pattern, countries))
    return countries_ends_with
    
print(categorize_countries())

# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.

def value_of_countries_with_letter():
    import string
    list_of_keys = list(string.ascii_uppercase)
    dct = {}

    for key in list_of_keys:
        dct[key] = len(list(filter(lambda country : country.startswith(key), countries)))

    return dct

print(value_of_countries_with_letter())
    

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.

def get_first_ten_countries():
    return countries[0:10]

print(get_first_ten_countries())

# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

def get_last_ten_countries():
    return countries[-11:-1]

print(get_last_ten_countries())

# Exercises: Level 3
# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:

from countries_data import countries_data

# Sort countries by name, by capital, by population
# Sort out the ten most spoken languages by location.
# Sort out the ten most populated countries.