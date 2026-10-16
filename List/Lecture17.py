# List comprehension
# List comprehensions are used to create new lists from existing iterables such as lists, tuples, dictionaries, sets, arrays, or even strings
# syntax 

# example_list = [expression(item) for item in iterable if condition]
names = ["Milo", "Saurabh", "Bob", "Avantika", "golii"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

# List Method 
# Using in index() method too find the index of value
names = ["Milo", "Saurabh", "Ayush", "Avantika", "golii"]
num = [1,2,3,4,5,6,7,8]
print(names.index("Ayush"))
print(num.index(3))

# Using in Reverse() Method in python 
names = ["Milo", "Saurabh", "Ayush", "Avantika", "golii"]
num = [1,2,3,4,5,6,7,8]
print(names.reverse)
print(num.reverse)

# Using in count() method to count the value in repeating in list 
colors = ["violet", "green", "indigo", "blue", "green"]
print(colors.count("green"))
 
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.count(2))

# Use the sort() is use to sort the similar type of element in list
names = ["Milo", "Saurabh", "Ayush", "Avantika", "golii"]
num = [1,2,3,4,5,6,7,8]
print(names.sort)
print(num.sort)
