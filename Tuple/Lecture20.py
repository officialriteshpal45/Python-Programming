# Tuple :- tuple can contain the multiple type of variable its work just like a list but data con't be change in tuple
# Example of tuple

tuple1 = (1, 2, 2, 3, 5, 4, 6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)

#tuple indexing
country = ("Spain", "Italy", "India", "England", "Germany")
print(country[1])
print(country[3])
print(country[0])

# negative indexing
print(country[-1])
print(country[-3])
print(country[-4]) 

# Find the City in existing in tuple
country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")

# Range in tuple
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])    
print(animals[-7:-2])     

# Tuple Manipulating
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")     
temp.pop(3)                 
temp[2] = "Finland"         
countries = tuple(temp)
print(countries)