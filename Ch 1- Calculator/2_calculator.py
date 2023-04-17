# Takes three inputs

num1 = float(input("enter the 1st num:")) # Variable declaration
num2 = float(input("enter the 2nd num:"))

which_op = input("enter which type of calculation you need:")

print(which_op)
print(type(which_op))

print(num1)
print(type(num1))

# Built-in functions: input, print, float (to do type casting), type (get the type of the variable)

if which_op == "add":
    print(num1 + num2)

elif which_op == "subtract":
    print(num1 - num2) 

elif which_op == "multiply":
    print(num1 * num2) 

elif which_op == "divide":
    # Preemptively checking for ZeroDivisionError.

    if num2 == 0:
        print("divisor can't be zero")
    else:
        print(num1 / num2)

elif which_op == "power":
    print(num1 ** num2)  

elif which_op == "remainder": # This is also called modulo.
    print(num1 % num2)          
else:
    print("please enter a valid operation")