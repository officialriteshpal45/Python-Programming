# Perform the operation in List 

# Add List Items using in 3 way - append(), insert(), and extend()

# 1. append() its store the data  in the last index vlaue 
student_name = [" Pardeep " , " Vipin " , " Golu " , " Ansh "]
student_name.append(" Keshav " )# Data is store in last index value 
print(student_name)

# 2. insert() its store the data in user according 
student_name = [" Pardeep " , " Vipin " , " Golu " , " Ansh "]
student_name.insert(1,("Sandeep"))
print(student_name)

# 3. extend() : This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list
list1 = ["Red" , "Blue" ,"Green"]
list2 = ["Yellow" , " Black" , " Sky "]
list1.extend(list2)
print(list1)