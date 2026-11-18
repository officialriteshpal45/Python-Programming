# WRITE A FUNCTION TO CONVERT USD TO INR
import math
def convertor(usd_val):
    inr_val = usd_val * 95
    print(usd_val, "USD =", inr_val, "INR")

convertor(2500)
# Return statement in function

# Write a calculator program in using in function
def cal( a , b ):
    print("sum of two number :-", a + b)
    print("sub of two number :-", a - b)
    print("mul of two number :-", a * b)
    print("div of two number :-", a / b)

cal(5 , 6 )
cal(2 , 2)

