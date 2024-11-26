# Exercises: Level 1
# Writ a function which generates a six digit/character random_user_id.
#   print(random_user_id());
#   '1ee33d'

import random

def random_user_id():
    user_id = ""
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    count = 0
    
    while count < 6:
        user_id = user_id + characters[random.randint(0, len(characters) - 1)]
        count += 1
        
    return user_id

print(random_user_id())

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) # user input: 5 5
# #output:
# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf

def user_id_gen_by_user():
    max_num_chars = int(input("How many characters do you want? "))
    num_of_IDs = int(input("How many IDs do you want? "))
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    count = 0

    while count < num_of_IDs: 
        count2 = 0
        user_id = ""

        while count2 < max_num_chars:
            user_id = user_id + characters[random.randint(0, len(characters) - 1)]
            count2 += 1

        print(user_id)
        count += 1
        
user_id_gen_by_user()

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form

def rgb_color_gen():
    numbers = []

    for number in range(0, 256):
        numbers.append(number)

    num1 = random.randint(0, len(numbers))
    num2 = random.randint(0, len(numbers))
    num3 = random.randint(0, len(numbers))
    
    return f'rgb({num1}, {num2}, {num3})'

print(rgb_color_gen())

# Exercises: Level 2
# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

def list_of_hexa_colors():
    characters = "abcdef0123456789"
    max_times = random.randint(1, 5)
    count = 0
    hexadecimal_color = ""

    while count < max_times:
        count2 = 0
        string = ""

        while count2 < 6:
            string = string + characters[random.randint(0, 15)]
            count2 += 1

        hexadecimal_color = hexadecimal_color + "#" + string + " "
        count += 1

    return hexadecimal_color.split()
    
print(list_of_hexa_colors())

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

def list_of_rgb_colors():
    numbers = []
    rgb_colors = ""
    max_times = random.randint(1, 5)
    count = 0
    
    for number in range(0, 256):
            numbers.append(number)

    while count < max_times:
        num1 = str(random.randint(0, len(numbers)))
        num2 = str(random.randint(0, len(numbers)))
        num3 = str(random.randint(0, len(numbers)))
    
        rgb_colors = rgb_colors + "rgb(" + num1 + "," + num2 + "," + num3 + ")" + " " 
        count += 1
    
    return rgb_colors.split()

print(list_of_rgb_colors())

# Write a function generate_colors which can generate any number of hexa or rgb colors.
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']

def generate_colors(type_color, total_colors):
    hexa_or_rgb = type_color
    total_of_colors = total_colors

    if hexa_or_rgb == "hexa":
        characters = "abcdef0123456789"
        max_times = total_of_colors
        count = 0
        hexadecimal_color = ""

        while count < max_times:
            count2 = 0
            string = ""

            while count2 < 6:
                string = string + characters[random.randint(0, 15)]
                count2 += 1

            hexadecimal_color = hexadecimal_color + "#" + string + " "
            count += 1

        return hexadecimal_color.split()

    elif hexa_or_rgb == "rgb":
        numbers = []
        rgb_colors = ""
        max_times = total_of_colors
        count = 0

        for number in range(0, 256):
                numbers.append(number)

        while count < max_times:
            num1 = str(random.randint(0, len(numbers)))
            num2 = str(random.randint(0, len(numbers)))
            num3 = str(random.randint(0, len(numbers)))

            rgb_colors = rgb_colors + "rgb(" + num1 + "," + num2 + "," + num3 + ")" + " " 
            count += 1

        return rgb_colors.split()
    
print(generate_colors("hexa", 3))
print(generate_colors("hexa", 5))
print(generate_colors("rgb", 3))
print(generate_colors("rgb", 5))

# Exercises: Level 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

def shuffle_list(list):
    random.shuffle(list)
    return list

print(shuffle_list(["Python", "SQL", "Linux"]))

# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

def array_of_unique_nums():
    new_set = set()
    count = 0

    while count < 7:
        new_set.add(random.randint(0, 9))
        count += 1

    new_list = list(new_set)
    return new_list

print(array_of_unique_nums())