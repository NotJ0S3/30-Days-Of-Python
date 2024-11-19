# Exercises: Level 1
# Declare an empty list
list = []

# Declare a list with more than 5 items
items_list = ["Laptop", "Keyboard", "Mouse", "Headphones", "Monitor"]

# Find the length of your list
len_of_list = len(items_list)

# Get the first item, the middle item and the last item of the list
first_item = items_list[0]
middle_item = items_list[2]
last_item = items_list[-1]

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["J0S3", 20, 1.80, "4everAlone", "Las Vegas"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0])
print(it_companies[int(len(it_companies) / 2)])
print(it_companies[-1])

# Print the list after modifying one of the companies
it_companies[4] = "Xbox"
print(it_companies)

# Add an IT company to it_companies
it_companies.append("PlayStation")

# Insert an IT company in the middle of the companies list
it_companies.insert(int(len(it_companies) / 2), "Nintendo")

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()

# Join the it_companies with a string '#;  '
it_companies2 = '#;  '.join(it_companies)
print(it_companies2)

# Check if a certain company exists in the it_companies list.
does_exist = "Xbox" in it_companies
print(does_exist)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
first_3_companies = it_companies[:3]
print(first_3_companies)

# Slice out the last 3 companies from the list
last_3_companies = it_companies[-3:]
print(last_3_companies)

# Slice out the middle IT company or companies from the list
middle_it_companies = it_companies[int(len(it_companies) / 2)]
print(middle_it_companies)

# Remove the first IT company from the list
it_companies.remove("Xbox")
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies.pop(int(len(it_companies) / 2))
print(it_companies)

# Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists:

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_and_back = front_end + back_end
print(front_and_back)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_and_back.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)


# Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
ages_min = min(ages)
ages_max = max(ages)

# Add the min age and the max age again to the list
ages.append(ages_min)
ages.append(ages_max)

# Find the median age (one middle item or two middle items divided by two)
ages_median = ages[int((len(ages) - 2) / 2)] / 2

# Find the average age (sum of all items divided by their number )
ages_average = (sum(ages[0:10])) / (len(ages) - 2)

# Find the range of the ages (max minus min)
ages_range = ages_max - ages_min

# Compare the value of (min - average) and (max - average), use abs() method
print(abs(ages_min - ages_average and ages_max - ages_average))

# Find the middle country(ies) in the countries list
countries_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_country = countries_list[int(len(countries_list) / 2)]

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half = countries_list[0:4]
second_half = countries_list[4:]

# Unpack the first three countries and the rest as scandic countries.
first_country, second_country, third_country, *scandic_countries = countries_list
