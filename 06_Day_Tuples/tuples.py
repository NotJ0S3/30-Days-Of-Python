# Exercises: Level 1
# Create an empty tuple
empty_tuple = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Pepito", "Juanito")
sisters = ("Fulanita", "Federica")

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# How many siblings do you have?
print(f'I have {len(siblings)} siblings')

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
family_members.append("Francisco")
family_members.append("Lucianita")

# Exercises: Level 2
# Unpack siblings and parents from family_members
sibling1, sibling2, sibling3, sibling4, *parents = family_members
print(sibling1)
print(sibling2)
print(sibling3)
print(sibling4)
print(parents)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("apple", "orange", "mango")
vegetables = ("carrot", "onion", "lettuce")
animals = ("Cow", "Chicken", "Fish")

food_staff_tp = fruits + vegetables + animals

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_staff_lt = list(food_staff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_tp_sliced = food_staff_tp[int(len(food_staff_tp) / 2)]

# Slice out the first three items and the last three items from food_staff_lt list
food_lt_first_3_items = food_staff_lt[:3]
food_lt_last_3_items = food_staff_lt[-3:]

# Delete the food_staff_tp tuple completely
del food_staff_tp

# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
