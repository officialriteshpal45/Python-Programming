# Nested Statement :- If else & elif
Child =int(input(" Enter The child Age "))
is_genz = True 

if (Child <= 5) :
    if is_genz :
       print(" child to drink Polio drop ")

    else:
      print(" Child Age is 5+ ")

else:
   print(" Greater Then 5 ")

# Switch (match ) Statement : It is similar to the switch statement bcz Switch is exist in other programming language

age = int(input("Enter a age :- "))

match (age) :
 case 18 :
  print ("Age is 18")

 case 12 :
  print(" Not eligible for movies ")

 case 50 :
   print ("You'r alse watching in movies ")

 case 0 :
    print(" Nothing ")
