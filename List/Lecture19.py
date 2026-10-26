# Nested list
Class10 = [
    ["Ritesh",21],
    ["Rahul",20],
    ["Ayush",33],
    ["Athrva",21],
    ["Divaya",20]
]
print(Class10)

# Accessing elements inside nested lists
Class10 = [
    ["Ritesh", 21],
    ["Divya", 20],
    ["Rahul", 20]
]

print(Class10[0][0])     
print(Class10[1][1]) 

# Modifying nested list items
Class10 = [
   ["Ritesh", 21],
   ["Divya", 20],
   ["Rahul", 20]
]

Class10[0][1] = 25      

print(Class10)

# Looping through nested lists
Class10 = [
    ["Ritesh",21],
    ["Rahul",20],
    ["Ayush",33],
    ["Athrva",21],
    ["Divaya",20]
]

for Class in Class10 :
    print(Class10)

# Matrix representation using nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])       # Row 1, Column 2    