# WRITE A FUNCTION TO CONVERT USD TO INR
def convertor(usd_val):
    inr_val = usd_val * 95
    print(usd_val, "USD =", inr_val, "INR")

convertor(2500)
# Return statement in function
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))