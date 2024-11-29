# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negative_zero_nums = [i for i in numbers if i < 0]
print(negative_zero_nums)

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

flattened_list = [number for row1 in list_of_lists for row2 in row1 for number in row2]
print(flattened_list)

# Using list comprehension create the following list of tuples:

# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]

list_of_numbers = [(i, 1, i * 1, i * i, i ** 3, i ** 4, i ** 5) for i in range(11)]
print(list_of_numbers)

# Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

flattened_countries = [[country.upper(), country[:3].upper(), capital.upper()] 
             for sublist in countries for country, capital in sublist]
print(flattened_countries)

# Change the following list to a list of dictionaries:

# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]

dict_list = [{'country': country.upper(), 'city': capital.upper()} 
             for sublist in countries for country, capital in sublist]

print(dict_list)

# Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

flattenes_names = [sublist2[0] + " " + sublist2[1] for sublist in names for sublist2 in sublist]

print(flattenes_names)

# Write a lambda function which can solve a slope or y-intercept of linear functions.

y = lambda x1, x2, y1, y2: (abs(((y2 - x2) / (y1 - x1))) + x2) / x1

print(y(1, 4, 3, -2))