# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
# Declare a variable named company and assign it to an initial value "Coding For All".
# Print the variable company using print().
# Print the length of the company string using len() method and print().
# Change all the characters to uppercase letters using upper() method.
# Change all the characters to lowercase letters using lower() method.
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
# Cut(slice) out the first word of Coding For All string.
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
# Replace the word coding in the string 'Coding For All' to Python.
# Change Python for Everyone to Python for All using the replace method or other methods.
# Split the string 'Coding For All' using space as the separator (split()) .
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
# What is the character at index 0 in the string Coding For All.
# What is the last index of the string Coding For All.
# What character is at index 10 in "Coding For All" string.
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
# Create an acronym or an abbreviation for the name 'Coding For All'.
# Use index to determine the position of the first occurrence of C in Coding For All.
# Use index to determine the position of the first occurrence of F in Coding For All.
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Does ''Coding For All' start with a substring Coding?
# Does 'Coding For All' end with a substring coding?
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

str1 = "Thirty"
str2 = "Days"
str3 = "Of"
str4 = "Python"
full_str = str1 + str2 + str3 + str4
print(full_str)

msg1 = "Coding"
msg2 = "For"
msg3 = "All"
full_msg = msg1 + msg2 + msg3
print(full_msg)

company = "Coding For All"

print(company)

print(len(company))

print(company.isupper())

print(company.islower())

print(company.capitalize().title().swapcase())

first_word = company[0:5]
print(first_word)

print(company.find("Coding"))

print(company.replace("Coding", "Python"))

phrase = "Python for Everyone"
print(phrase.replace("Python For Everyone", "Python For All"))

print(company.split(" "))

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(","))

print(company[0])

print(company[-1])

print(company[10])

print(phrase.replace("Python", "Py"))

print(company.replace("Coding", "Code"))

print(company.index("C"))

print(company.index("F"))

print(company.rfind("l"))

new_phrase = "You cannot end a sentence with because because because is a conjunction"
print(new_phrase.find("because"))

print(new_phrase.rfind("because"))

print(new_phrase[31:54])

print(company.startswith("Coding"))

print(company.endswith("Coding"))

new_company = '   Coding For All      '

print(new_company.strip(" "))

phrase1 = "30DaysOfPython"
phrase2 = "thirty_days_of_python"
print(phrase1.isidentifier())
print(phrase2.isidentifier())

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(python_libraries))

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsin")

radius = 10
pi = 3.14

print("area = {} x {} ^ {} = {}".format(pi, radius, 2, pi * radius ** 2))
print(f"The are of a circle with radius {radius} is {pi * radius ** 2}")

a = 8
b = 6

print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')