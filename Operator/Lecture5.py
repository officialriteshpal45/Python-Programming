# Operator in python :- Arithmatic Operator , Relational ,
# 1. Arithmatic Operator
a = 15
b = 4

print("Addition of a + b :- ", a + b)  

print("Subtraction of a - b :- ", a - b) 

print("Multiplication of a * b :- ", a * b)  

print("Division of a / b :- ", a / b) 

print("Floor Division:", a // b)  

print("Modulus:", a % b) 

print("Exponentiation:", a ** b)

# 2. Relational Operator : - It's return a true or false vlue

print("The ans of a > b ", a>b)
print("The ans of a < b " ,a<b)
print("The ans of a >= b ", a>=b)
print("The ans of a <= b ",a<=b)
print("The ans of a != b ",a!=b)
print("The ans of a == b " ,a == b)

# 3. logical operator :- Combine two value to use this operator 
# AND 
print("True and False is :- ", True and False)
print("False and False is :- ", False and False)
print("True and True is :- ", True and True)
print("False and True is :- ", False and True)

# OR
print("True and False is :- ", True or False)
print("False and False is :- ", False or False)
print("True and True is :- ", True and True)
print("False and True is :- ", False and True)

# NOT
print("True is :-", not True)
print("False is :-", not False)

# 4. Assignment Operator
b = a
print("The ans is b = a :-",b)
b += a
print("The ans is b += a :-",b)
b -= a
print("The ans is b -= a :-",b)
b *= a
print("The ans is b *= a :-",b)
b <<= a
print("The ans is b <<= a :-",b)

# 5. Identity Operator 
c = a
print(a is not b)
print(a is c)
