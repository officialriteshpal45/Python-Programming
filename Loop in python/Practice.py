# Print Trangle 
for i in range(1, 5):
    for j in range(i):
        print(end=' * ' )
    print()

# Print piramid using in python 
rows = 5

for i in range(1, rows + 1):
    # Print leading spaces, followed by odd numbers of stars
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)