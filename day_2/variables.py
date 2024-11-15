#Exercises: Level 1

# Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
# Write a python comment saying 'Day 2: 30 Days of python programming'
# Declare a first name variable and assign a value to it
# Declare a last name variable and assign a value to it
# Declare a full name variable and assign a value to it
# Declare a country variable and assign a value to it
# Declare a city variable and assign a value to it
# Declare an age variable and assign a value to it
# Declare a year variable and assign a value to it
# Declare a variable is_married and assign a value to it
# Declare a variable is_true and assign a value to it
# Declare a variable is_light_on and assign a value to it
# Declare multiple variable on one line

# Day 2: 30 Days of python programming

first_name = "Not"
last_name = "J0S3"
full_name = "NotJ0S3"
country = "Francia"
city = "Paris"
age = 20
year = 2025
is_married = True
is_true = False
is_light = ["Yes", "No"]
is_light_on = {"Yes":True, "No":False}
first_name, last_name, country, age, is_married = "Not", "J0S3", "Colombia", 20, False

# Exercises: Level 2

# Check the data type of all your variables using type() built-in function
# Using the len() built-in function, find the length of your first name
# Compare the length of your first name and your last name
# Declare 5 as num_one and 4 as num_two
# Add num_one and num_two and assign the value to a variable total
# Subtract num_two from num_one and assign the value to a variable diff
# Multiply num_two and num_one and assign the value to a variable product
# Divide num_one by num_two and assign the value to a variable division
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
# Calculate num_one to the power of num_two and assign the value to a variable exp
# Find floor division of num_one by num_two and assign the value to a variable floor_division
# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))
print(type(is_light))
print(type(is_light_on))

print(len(first_name))
print("My length first name is: ", len(first_name), " and my last name lenght is: ", len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
dif = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

circle_radius = 30

area_of_circle = 3.14 * (circle_radius ** 2)
circum_of_circle = 2 * 3.14 * circle_radius

print("Number one:", num_one)
print("Number two:", num_two)
print("Total: ", total)
print("Diference: ", dif)
print("Product: ", product)
print("Division: ", division)
print("Remainder: ", remainder)
print("Exponential: ", exp)
print("Floor division: ", floor_division)
print("Circle radius: ", circle_radius)
print("Circle are: ", area_of_circle)
print("Circle circum: ", circum_of_circle)

circle_radius = float(input("What is the radius of your circle?"))

area_of_circle = 3.14 * circle_radius ** 2
circum_of_circle = 2 * 3.14 * circle_radius

print("Circle are: ", area_of_circle)
print("Circle circum: ", circum_of_circle)

first_name = input("What is your first name?")
last_name = input("What is your last name?")
country = input("What is your country?")
city = input("What is your city?")
age = input("What is your age?")

print("Hello", first_name, last_name, "from", city, ",", country, ". Nice to know your age is", age)