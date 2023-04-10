num1 = float(input("enter the 1st num "))
num2 = float(input("enter the 2nd num "))
which_type = input("enter which type of calculation you need ")
if which_type == "add":
    print(num1 + num2)
elif which_type == "subtract":
    print(num1 - num2) 
elif which_type == "multiply":
    print(num1 * num2) 

elif which_type == "divide":
    if num2 == 0:
        print("divisor can't be zero")
    else:
        print(num1 / num2)
elif which_type == "power":
    print(num1 ** num2)  
elif which_type == "remainder":
    print(num1 % num2)          
else:
    print("please enter a valid operation")