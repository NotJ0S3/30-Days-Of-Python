# Exercises: Level 1
# What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
#     [
#     (6, 'love'),
#     (5, 'you'),
#     (3, 'can'),
#     (2, 'what'),
#     (2, 'teaching'),
#     (2, 'not'),
#     (2, 'else'),
#     (2, 'do'),
#     (2, 'I'),
#     (1, 'which'),
#     (1, 'to'),
#     (1, 'the'),
#     (1, 'something'),
#     (1, 'if'),
#     (1, 'give'),
#     (1, 'develop'),
#     (1, 'capabilities'),
#     (1, 'application'),
#     (1, 'an'),
#     (1, 'all'),
#     (1, 'Python'),
#     (1, 'If')
#     ]

import re

words_list = set(paragraph.split())
matches = [tuple([len(re.findall(words, paragraph)), words]) for words in words_list]
matches.sort(reverse=True)
print(matches)

# The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
# points = ['-12', '-4', '-3', '-1', '0', '4', '8']
# sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
# distance = 8 -(-12) # 20

points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points = [int(num) for num in points]
distance = max(sorted_points) - min(sorted_points)
print(distance)

# Exercises: Level 2
# Write a pattern which identifies if a string is a valid python variable

# is_valid_variable('first_name') # True
# is_valid_variable('first-name') # False
# is_valid_variable('1first_name') # False
# is_valid_variable('firstname') # True

def is_valid_variable(var_name):
    regex_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    match = re.match(regex_pattern, var_name)
    if match:
        print(True)
    else:
        print(False)

is_valid_variable('first_name')
is_valid_variable('first-name')
is_valid_variable('1first_name') 
is_valid_variable('firstname')

# Exercises: Level 3
# Clean the following text. After cleaning, count three most frequent words in the string.

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(txt):
    matches = re.sub('(\$|#|%|&|@)', '', txt)
    return matches

print(clean_text(sentence))
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher

def most_frequent_words(clean_text):
    words_list = set(clean_text.split())
    matches = [tuple([len(re.findall(words, clean_text)), words]) for words in words_list]
    matches.sort(reverse=True)
    return matches[1:4]

print(most_frequent_words(clean_text(sentence))) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
