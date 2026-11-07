# Dictionaries in python
# Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

# Output
# {'name': 'Karan', 'age': 19, 'eligible': True}

# Access Items
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))

# Accessing Multiple Values
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

# Accessing Keys
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())

# Accessing Key-Value Pairs
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())

# Add/Remove Items
# Add - Adding items to a dictionary
info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)
info['DOB'] = 2001
print(info)

# Use the update() method
info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)
info.update({'age': 20})
info.update({'DOB': 2001})
print(info)