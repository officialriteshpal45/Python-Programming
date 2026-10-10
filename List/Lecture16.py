# Remove list element in python using Python method 
# pop() - delete last value of list 
data = [ 45 , 84 , 69 , 87 , 85 ]
data.pop()
print(data)

# Remove item in indexing 
data = [ 45 , 84 , 69 , 87 , 85 ]
data.pop(2)# pass parameter 2 
print(data)

# Remove :- this method also delete in spesific element 
data = [ 45 , 84 , 69 , 87 , 85 ]
data.remove(69)
print(data)

# delete :- its not a method it is a keyword to delete the the specific keyword in python
colors = ["violet", "indigo", "blue", "green", "yellow"]
del colors[3]
print(colors)

# clear : its clear all element in the list 
colors = ["violet", "indigo", "blue", "green", "yellow"]
colors.clear()
print(colors)

# change list item 
names = ["keshav", "Puspa", "Mangal", " Jagga ", "SHEKHAWAT"]
names[2] = "Millie"
print(names)

