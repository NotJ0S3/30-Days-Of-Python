# Declare your age as integer variable
# Declare your height as a float variable
# Declare a variable that store a complex number
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
#     Enter side a: 5
#     Enter side b: 4
#     Enter side c: 3
#     The perimeter of the triangle is 12
# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Compare the slopes in tasks 8 and 9.
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
# There is no 'on' in both dragon and python
# Find the length of the text python and convert the value to float and convert it to string
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# Check if type of '10' is equal to type of 10
# Check if int('9.8') is equal to 10
# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.
# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125  

age = 20
height = 1.80
complex_num = 2 + 2j

triangle_base = float(input("Enter the base of your triangle: "))
triangle_height = float(input("Enter the height of your triangle: "))
triangle_area = 0.5 * triangle_base * triangle_height

print("The area of your triangle is: ", triangle_area)

triangle_sideA = float(input("Whats is the length of the side A of your triangle?: "))
triangle_sideB = float(input("Whats is the length of the side B of your triangle?: "))
triangle_sideC = float(input("Whats is the length of the side C of your triangle?: "))
triangle_perimeter = triangle_sideA + triangle_sideB + triangle_sideC

print("The perimeter of your triangle is: ", triangle_perimeter)

rectangle_length = float(input("What is the length of your rectangle?: "))
rectangle_width = float(input("What is the width of your rectangle?: "))
rectangle_area = rectangle_length * rectangle_width
rectangle_perimeter = 2 * (rectangle_length + rectangle_width)

print("The area of your rectangle is: ", rectangle_area)
print("The perimeter of your rectangle is: ", rectangle_perimeter)

pi = 3.14
circle_radius = float(input("What is the radius of your circle?: "))
circle_area = pi * circle_radius * circle_radius
circle_circumference = 2 * pi * circle_radius

print("The area of your circle is: ", circle_area)
print("The circumference of your circle is: ", circle_circumference)

slope = 2
b = 2
y_intercept = slope * 0 - b
x_intercept = (b + 0) / slope
print("The x intercept is: ", x_intercept, " and the y intercept is: ", y_intercept)

x1 = 6
x2 = 10
y1 = 2
y2 = 2
m = (y2 - y1) / (x2 - x1)
print("The slope of x(2, 2) and y(6, 10) is: ", m)

print("The slope 1 and slope 2 are equal? ", slope == m)

x = float(input("Give me a value for X:"))
y = x ** 2 + 6 * x + 9
print("The value for Y is: ", y)

print(len('python') == len('dragon'))
print("Is 'on' in 'python'?: ", "on" in "python", "and in 'dragon'?: ", "on" in "dragon")

message = "I hope this course is not full of jargon"
print("Is 'jargon' in the message?: ", 'jargon' in message)

print(str(float(len("Python"))))

num = float(input("Give me a number: "))
odd = num % 2
print("Your number is Even?: ", odd == 0)
print("Your number is Odd: ", odd != 0)

print(7 // 3 == int(2.7))

print(type('10') == type(10))

print(int(9.8) == 10)

hour = int(input("How much hours do you work per week?: "))
rate_per_hours = int(input("How much do you get paid per hour?: "))
pay = hour * rate_per_hours
print("You get paid monthly: ", pay)

num_of_years = float(input("What is the number of years you have lived? "))
seconds_of_years = (num_of_years * 365) * 86400
print("You have been lived for ", seconds_of_years, " seconds")

print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 2 7")
print("4 1 4 16 64")
print("5 1 5 25 125")