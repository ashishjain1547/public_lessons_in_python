import math

x=int(input("Enter The Number to be Operated:"))
op=input("Enter the Operator to be used on the number:")
if op == "not" or op == "~":
    print(bin(x))
    print(bin(~x))
    print (~x)

elif op == "square root":
    print(x**(1/2))
# elif op == "floor":
#     print(math.floor(x))
elif op == "cube root":
    print(x**(1/3))
else:
    print("Invalid operator")