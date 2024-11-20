# Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to drive.")
else:
    print(f'You need {18 - age} more years to learn to drive.')


# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:  

# Enter your age: 30
# You are 5 years older than me.

my_age = 25
your_age = int(input("Enter your age: "))

if your_age > my_age:
    print(f'You are {your_age - my_age} years older than me')
elif your_age < my_age:
    print(f'I am {my_age - your_age} years older than you')
else:
    print("We are the same age")


# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')


# Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:

# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

student_grade = int(input("What is your score? "))

if student_grade >= 80 and student_grade <= 100:
    print(f'Your score is {student_grade} so your grade is A')
elif student_grade >= 70 and student_grade <=79:
    print(f'Your score is {student_grade} so your grade is B')
elif student_grade >= 60 and student_grade <=69:
    print(f'Your score is {student_grade} so your grade is C')
elif student_grade >= 50 and student_grade <=59:
    print(f'Your score is {student_grade} so your grade is D')
elif student_grade >=0 and student_grade <= 49:
    print(f'Your score is {student_grade} so your grade is F')
else:
    print("Wrong score! Your score has to be between 0 and 100")


# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

month = input("What is the month? ")
Autum = ["September", "October", "November"]
Winter = ["December", "January", "February"]
Spring = ["March", "April", "May"]
Summer = ["June", "July", "August"]

if month in Autum:
    print(f'The month is {month} so you are in Autum')
elif month in Winter:
    print(f'The month is {month} so you are in Winter')
elif month in Spring:
    print(f'The month is {month} so you are in Spring')
elif month in Summer:
    print(f'The month is {month} so you are in Summer')
else:
    print("Thats not a month of the year. Or remember that months star with a capital letter")


# The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

new_fruit = input("Give me a new fruit to put on the list ")
not_numbers = "1234567890"

if type(new_fruit) == str and new_fruit not in not_numbers:
    if new_fruit not in fruits:
        fruits.append(new_fruit)
        print(fruits)
    else:
        print("That fruit already exist in the list!")
else:
    print("That can not be a fruit")


# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!

person={
    'first_name': 'Not',
    'last_name': 'J0S3',
    'age': 20,
    'country': 'Norway',
    'is_marred': False,
    'skills': ['Python', 'Django', 'SQL', 'AWS', 'Pentesting'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.

if "skills" in person:
    skills_values = person["skills"]
    print(skills_values[int(len(skills_values)/2)])
    if "Python" in skills_values:
        print(f'{"Python" in skills_values}, Python is in skills')
    else:
        print(f'{"Python" in skills_values}, Python is not in skills')
    if "JavaScript" or "React" in skills_values:
        print("He is a front end developer")
    elif "Node" or "Python" or "MongoDB" in skills_values:
        print("He is a back end developer")
    elif "React" and "Node" and "MongoDB" in skills_values:
        print("He is a full stack developer")
    else:
        print("unknown title")
        
if "is_married" is True and "country" is "Finland":
    print(f'{person["first_name"]} lives in {person["country"]} and he is married')
else:
    print(f'{person["first_name"]} lives in {person["country"]} and he is not married')
