# variable :- Variable is a name given to a memory location that stores data 
#There are two type of variable in python 
# 1. Local variable 
icecream = "Vanilla"    # global variable :- Global variable declaring in Out of the function 
def foods():
    vegetable = "Potato"    # local variable :- Declaring in the inside the function 
    fruit = "Lichi"         # local variable
    print(vegetable + " is a local variable value.")
    print(fruit + " is a local variable value.")

foods()

# 2. Global Variable 
icecream = "Vanilla"    # global variable :- Global variable declaring in Out of the function 
def foods():
    print(icecream + " is a global variable value.")

# python explicit (Don't need to declare variable type)
name= "Ritesh pal"#name is the variable and "Ritesh pal" is the value assigned to the variable
print(name)# string variable
print(type(name))#print type of variable

age =22
print(age)#integer variable
print(type(age))

Course = "AI Era"
print(Course)
print(type(Course))

CGPA=7.3#CGPA is the variable and 7.3 is the value assigned to the variable
print(CGPA)#float variable
print(type(CGPA))

# Method to declared variable in python 
Color = "yellow"    # valid variable name
cOlor = "red"       # valid variable name
_color = "blue"     # valid variable name

# 5color = "green"    # invalid variable name
# $color = "orange"   # invalid variable name
