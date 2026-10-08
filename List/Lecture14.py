# List indexing 
lst =     [49 , 0 , 5 , 85 , 52 , 52 , 55 , 2 ]
#indexing  [0] [1] [2]  [3]   [4]  [5]   [6]  [7]
print(lst[3]) # 85

# Negative Indexing 

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])

# Check colors exist using ( in ) keyword 
if "Yellow" in colors :
    print(" Yellow is exist in the list ")
else :
    print(" Yellow can't be exist in the list ")

# check color is not exist 
if "pink" in colors :
    print(" pink is exist in the list ")
else :
    print(" pink can't be exist in the list ")

# Range in list 
lst2 =     [49 , 0 , 5 , 85 , 52 , 52 , 55 , 2 ]

print(lst2[3:7])  # using positive indexes
print(lst2[-7:-2])  # using negative indexes