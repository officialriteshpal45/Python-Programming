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

#Using in Reverse() Method in python 
names = ["Milo", "Saurabh", "Ayush", "Avantika", "golii"]
num = [1,2,3,4,5,6,7,8]
print(names.reverse)
print(num.reverse)
