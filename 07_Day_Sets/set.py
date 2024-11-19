# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1  
# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add("Twitter")

# Insert multiple IT companies at once to the set it_companies
it_companies.update(["Xbox", "PlayStation", "Nintendo"])

# Remove one of the companies from the set it_companies
it_companies.remove("IBM")

# What is the difference between remove and discard
# The difference is remove will show an error if the item is not found and discard won't show anything
it_companies.discard("Amazon")

# Exercises: Level 2
# Join A and B
C = A.union(B)

# Find A intersection B
print(A.intersection(B))

# Is A subset of B
print(A.issubset(B))

# Are A and B disjoint sets
print(A.isdisjoint(B))

# Join A with B and B with A
A.union(B)
B.union(A)

# What is the symmetric difference between A and B
print(f'The symmetric difference between A and B are {A.symmetric_difference(B)}')

# Delete the sets completely
del A, B

# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(f"The length of 'age' as a list is {len(age)} and as a set is {len(age_set)}")

# Explain the difference between the following data types: string, list, tuple and set
print("'' An string is a combination of character. It could be letters, symbols, spaces and number (if they are characters with quotes)")
print("[] A list is where we can save many and different data type, with an index or position stating by 0, and we can modify this content")
print("() A tuple is like a list but here we can not modify and add his content. It is immutable")
print("{} And a set is like a tuple and list but we can add data, but not repeat the content. It is not ordered like in Math, unique items")

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
phrase = "I am a teacher and I love to inspire and teach people"
phrase_unique_words = len(set(phrase.split()))

print(f'There have been used {phrase_unique_words} unique words')
