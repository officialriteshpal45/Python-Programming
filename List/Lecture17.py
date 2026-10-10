# List comprehension
# List comprehensions are used to create new lists from existing iterables such as lists, tuples, dictionaries, sets, arrays, or even strings
# syntax 
example_list = [expression(item) for item in iterable if condition]

names = ["Milo", "Saurabh", "Bob", "Avantika", "golii"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)