# Using Loop :- loops are further classified into the following types: for loop, while loop, nested loops
# Loop 
colors = ("Red", "Green", "Blue", "Yellow")
for x in colors:
    print(x)

# while loop

count = 5
while (count > 0):
    print(count)
    count = count - 1

# nested loop 
while (i <= 3):
    for k in range(1, 4):
        print(i, "*", k, "=", (i * k))
    i = i + 1
    print()

    # print table in using in nested loop

    for i in range(1, 3):
     k = 1
    while (k <= 3):
        print(i, "*", k, "=", (i * k))
        k = k + 1
    print()

# Control Statements :- using in pass, continue, and break for control the statement

i = 1
while (i < 5):
     print(" Hello Python ") #It's not run so using in pass keyword in python
pass

for j in range(5):
    pass

if (i == 2):
    pass
