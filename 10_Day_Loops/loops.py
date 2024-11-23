# Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.
for number in range(0, 11):
    print(number)

number = 0

while number <= 10:
    print(number)
    number = number + 1

# Iterate 10 to 0 using for loop, do the same using while loop.
numbers = list(range(0, 11))
numbers.reverse()

for number in numbers:
    print(number)
    
number = 10

while number >= 0:
    print(number)
    number = number - 1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######

count = 0
output = "#"

while count < 7:
    print(output)
    output = output + "#"
    count = count + 1

# Use nested loops to create the following:

# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #

for i in range(0, 8):
    for j in range(0, 1):
        print("# # # # # # # #")

# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

for i in range(0, 11):
    print(f'{i} X {i} = {i * i}')

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

programming_list = ['Python', 'Numpy','Pandas','Django', 'Flask']

for lenguages in programming_list:
    print(lenguages)

# Use for loop to iterate from 0 to 100 and print only even numbers

for number in range(0, 101, 2):
    print(number)

# Use for loop to iterate from 0 to 100 and print only odd numbers

for number in range(0, 101):
    if number % 2 != 0:
        print(number)

# Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.

sum = 0

for number in range(0, 101):
    sum = sum + number
    print(sum)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.

sum_even = 0
sum_odd = 0

for number in range(0, 101, 2):
    sum_even = sum_even + number
    print(sum_even)

for number in range(0, 101):
    if number % 2 != 0:
        sum_odd = sum_odd + number
        print(sum_odd)

# Exercises: Level 3
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

from data.countries import countries

for country in countries:
    if "land" in country:
        print(country)

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits = ['banana', 'orange', 'mango', 'lemon']

index = len(fruits)
count = 0

while count < len(fruits):
    print(fruits[(index - 1) - count])
    count = count + 1
    
# Go to the data folder and use the countries_data.py file.

from data.countries_data import countries_data

# What are the total number of languages in the data

total_languages = set()

for dct in countries_data:
    total_languages.update(dct.get("languages"))
    
print(f'The total number of langaues in the data is: {len(total_languages)}')

# Find the ten most spoken languages from the data

all_languages = []

for dct in countries_data:
    all_languages.extend(dct.get("languages"))  

print(all_languages)


# Find the 10 most populated countries in the world
