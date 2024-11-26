# Exercises: Level 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def sum (a, b):
    total = a + b
    return total

print(sum(23, 90))

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def circle_area (radius):
    PI = 3.14
    area = PI * radius * radius
    return area

print(circle_area(50))

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums (*nums):
    total = 0
    for num in nums: 
        if type(num) == int or type(num) == float:
            total += num
        else:
            print("Please enter valid numbers. Ints or floats")    
    return total

print(add_all_nums(2, 34, 54))

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit (celcius):
    fahrenheit = (celcius * (9 / 5)) + 32
    return fahrenheit

print(convert_celsius_to_fahrenheit(32))

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season (month):
    Autum = ["September", "October", "November"]
    Winter = ["December", "January", "February"]
    Spring = ["March", "April", "May"]
    Summer = ["June", "July", "August"]

    if month in Autum:
        return print(f'The month is {month} so you are in Autum')
    elif month in Winter:
        return print(f'The month is {month} so you are in Winter')
    elif month in Spring:
        return print(f'The month is {month} so you are in Spring')
    elif month in Summer:
        return print(f'The month is {month} so you are in Summer')
    else:
        return print("Thats not a month of the year. Or remember that months star with a capital letter")
    
check_season("November")

# Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(a, b, c):
    x = (c - b) / a
    return x

print(calculate_slope(3, 5, 20))

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

import math

def solve_quadratic_eqn(a, b, c):
    if a != 0:
        x1 = -(b) + (math.sqrt((b ** 2) - (4 * a * c))) / 2 * a 
        x2 = -(b) - (math.sqrt((b ** 2) - (4 * a * c))) / 2 * a
    else:
        print(f"la funcion no puede ser cuadratica ya que {a} debe ser diferente de 0")
    return x1, x2

print(solve_quadratic_eqn(2, 3, -2))

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(new_list):
    for item in new_list:
        print(item)

print_list(["apple", "orange", "pineapple"])


# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(another_list = list):
    another_list.reverse()
    for item in another_list:
        print(item)
        
reverse_list(["Python", "SQL", "Linux"])

# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]

reverse_list([1, 2, 3, 4, 5])

# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]

reverse_list(["A", "B", "C"])

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(capital_list = list):
    for item in capital_list:
        print(item.capitalize())
    
capitalize_list_items(["python", "sQL", "linux"])

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']

def add_item(new_list = list, new_item = str):
    new_list.append(new_item)
    print(new_list)
    
add_item(food_staff, 'Meat')  # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']

# numbers = [2, 3, 7, 9]
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]

numbers = [2, 3, 7, 9]
add_item(numbers, 5)

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9]
# print(remove_item(numbers, 3))  # [2, 7, 9]

def remove_item(new_list = list, new_item = str):
    new_list.remove(new_item)
    print(new_list)
    
remove_item(food_staff, "Mango")
remove_item(numbers, 3)

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050

def sum_of_numbers(number):
    # num = 1
    sum = 0
    
    for num in range(1, number + 1):   # <----  Whit for loop
        sum = sum + num
    
    # while num <= number:   <---- Whit while loop
    #     sum = sum + num
    #     num += 1
        
    return sum
    
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(num):
    sum_odd = 0
    
    for number in range(1, num + 1):
        sum_odd = sum_odd + number
    
    return sum_odd
        
print(sum_of_odds(50))

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(num):
    sum_even = 0

    for number in range(0, num + 1, 2):
        sum_even = sum_even + number
    
    return sum_even

print(sum_of_even(50))

# Exercises: Level 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.

def evens_and_odds(value = int):
    if value > 0:
        total_even = []

        for number in range(0, value + 1, 2):
            total_even.append(number)
        
        total_odds = []
    
        for number in range(1, value + 1):
            if number % 2 != 0:
                total_odds.append(number)
    
    return f'The number of odds are {len(total_odds)} \nThe number of evens are {len(total_even)}'

print(evens_and_odds(100))

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(number):
    return math.factorial(number)

print(factorial(8))

# Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(value):
    return value is ""

print(is_empty(""))
print(is_empty("Hello!"))

# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

def calculate_mean(list_nums = list):
    sum_of_numbers = 0
    for number in list_nums:
        sum_of_numbers = sum_of_numbers + number
        
    mean = sum_of_numbers / len(list_nums)
    return mean

def calculate_median(list_nums = list):
    list_nums.sort()
    
    if len(list_nums) % 2 == 0:
        return list_nums[int(len(list_nums) / 2)], list_nums[int((len(list_nums) / 2) + 1)]
    else:
        return list_nums[int(len(list_nums) / 2)]

def calculate_mode(list_nums = list):
    key_dct = set(list_nums)
    values_dct = []
    final_dct = {}
    position = 0
    
    for num in key_dct:
        values_dct.append(list_nums.count(num))
        final_dct[num] = values_dct[position]
        position += 1
        
    reversed_dict = {value: key for key, value in final_dct.items()}
    
    target_value = max(values_dct)
    key = reversed_dict.get(target_value)
    
    return key


def calculate_range(list_nums = list):
    return max(list_nums) - min(list_nums)

def calculate_variance(list_nums = list):
    list1 = []
    sum_list1 = 0
    
    for num in list_nums:
        list1.append((num - calculate_mean(list_nums)) ** 2)
        
    for num in list1:
        sum_list1 = sum_list1 + num
        
    total = sum_list1 / len(list_nums)
        
    return total

def calculate_std(list_nums = list):
    return math.sqrt(calculate_variance(list_nums))

list_numbers = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

print(calculate_mean(list_numbers))
print(calculate_median(list_numbers))
print(calculate_mode(list_numbers))
print(calculate_range(list_numbers))
print(calculate_variance(list_numbers))
print(calculate_std(list_numbers))


# Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.

def is_prime(number):
    if number <= 1:
        return False
    
    for index in range(2, number):
        if number % index == 0:
            return False
        
    return True

print(is_prime(29))
print(is_prime(12))

# Write a functions which checks if all items are unique in the list.

def is_unique(list):
    is_unique = []
    
    for item in list:
        if list.count(item) > 1:
            is_unique.append(False)
        else:
            is_unique.append(True)
    
    return f'All the items in the list are unique: {all(is_unique)}'
        
print(is_unique([1, 2, 3, 3, 4, 4, 5, 6]))
print(is_unique([1, 2, 3, 4, 5, 6]))

# Write a function which checks if all the items of the list are of the same data type.

def same_type(list):
    is_same_type = []
    
    for item in range(0, len(list) - 1):
        if type(list[item]) == type(list[item + 1]):
            is_same_type.append(True)
        else:
            is_same_type.append(False)
    
    return all(is_same_type)
        
print(same_type([1, 2, 3, 4]))
print(same_type([1, 2, 3, "Hi"]))

# Write a function which check if provided variable is a valid python variable

def check_name_variable(var):
    list_of_reserve_words = ["False", "await", "else", "import", "pass", "None", "break", "except", "in", "raise", "True", "class", "finally", "is", "return", "and", "continue", "for", "lambda", "try", "as", "def", "from", "nonlocal", "while", "assert", "del" , "global", "not", "with", "async", "elif", "if", "or", "yield"]
    list_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if var is list_of_reserve_words or type(var[0]) is list_numbers:
        return f'The variable {var} can not be a variable name'
    else:
        return f'The variable {var} can be a variable name'
    
print(check_name_variable("0variable"))
    
# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

from data.countries_data import countries_data

# What are the total number of languages in the data

def total_languages(countries_data):
    total_languages = []

    for dct in countries_data:
        total_languages.extend(dct.get("languages"))

# Find the ten most spoken languages from the data

def most_spoken_languages(countries_data):
    value_spoken_language = {}
    total_languages = total_languages(countries_data)

    for language in total_languages:
        value_spoken_language[language] = total_languages.count(language)

    sorted_values = sorted(value_spoken_language.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_values[0:11] 

print(most_spoken_languages(countries_data))

# Find the 10 most populated countries in the world

def most_populated_countries(countries_data):
    new_keys = []
    new_values = []
    final_dct = {}
    position = 0
    
    for dct in countries_data:
        new_keys.append(dct.get("name"))
        new_values.append(dct.get("population"))
    
    for name in new_keys:
        final_dct[name] = new_values[position]
        position += 1
        
    sorted_dct = sorted(final_dct.items(), key=lambda x: x[1], reverse=True)
    return sorted_dct

print(most_populated_countries(countries_data))

# print(sorted_dct[0:11])