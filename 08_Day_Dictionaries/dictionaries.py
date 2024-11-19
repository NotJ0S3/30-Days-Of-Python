# Exercises: Day 8
# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Canela"
dog["color"] = "Brown"
dog["breed"] = "Mixed"
dog["legs"] = 4
dog["age"] = 5

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'Joseph',
    'last_name':'Martinez',
    'gender':'M',
    'age':30,
    'country':'Norway',
    'city':'Oslo',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(type(student["skills"]))

# Modify the skills values by adding one or two skills
student["skills"].append("SQL")

# Get the dictionary keys as a list
keys = student.keys()

# Get the dictionary values as a list
values = student.values()

# Change the dictionary to a list of tuples using items() method
print(student.items())

# Delete one of the items in the dictionary
student.popitem()

# Delete one of the dictionaries
del student
