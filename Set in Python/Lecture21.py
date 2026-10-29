# Set in python 
info = {"Aditya", 19, False, 5.9, 19}
print(info)

# Using a For loop
info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)

# Add/Remove Set Items
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

# Example 2 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

# Remove 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Seoul")
print(cities)