# Data type in python :- Data type is an attribute of data which tells the interpreter how the programmer intends to use the data
# These data types are divided into two categories: mutable and immutable
# 1. Mutable :- ist , dict , set , bytearra

fruits = ["apple", "banana", "cherry"]
print(id(fruits))  # Memory address before modification

fruits.append("mango")  # Adding a new item
print(fruits)
print(id(fruits))  # Same memory address → same object

# 2. Immutable :- int, float, complex, str, tuple, bool, bytes
name = "Harry"
print(id(name))  # Memory address before modification

name = name + " Potter"  # Concatenating creates a new string
print(name)
print(id(name))  # Different memory address → new object created

# There are three type of declared in string 
Name = "Ritesh Pal" # Most declaring string in python 
Name2 = ' Abhi ' #single string
Name3 = """ Shubham Sultan """ # Triple string
print(type(Name))#string data type
print(type(Name2))
print(type(Name3))

Roll_no = 101

print(type(Roll_no))#integer data type
Pass =True
print(type(Pass))#boolean data type

CGPA = 7.3
print(type(CGPA))#float data type
#These are the basic data types in python
