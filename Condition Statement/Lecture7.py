# Codition Statement Is use to Control the program Execution
# Threre are multiple Condition in python programming - If ,if else ,else if ,else ,switch
# 1. if Statement

Age =int(input("Enter Your Age :- "))

if(Age>17) :
    print("You are the voter for 2027 Election")

# 2. if else
if(Age>=18) :

    print("You'r Eligible for Voting")
else :

    print("You'r Not eligible for Vote")

# 3. elif if Statement Or ladder 
mark =int(input("Enter your mark :- "))

if mark>=33:
  print("Your are passed in exam ")

elif mark <= 33 :
    print("You'r Are Fail in Exam ")

elif(mark >= 60):
    print("Your grade is C ")

elif(mark >= 75):
    print("Your grade is B ")

elif(mark >= 85):
    print("Your grade is A ")

else :
    print(" Congratulation ")



