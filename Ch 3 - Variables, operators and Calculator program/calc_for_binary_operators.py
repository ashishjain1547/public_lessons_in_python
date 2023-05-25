instructions = """
Operations Supported : 
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Modulus
7. Percentage
8. Bitwise And
9. Bitwise Or
"""

x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))

op = input("Enter the operator that you want to use:")

if op == "percentage" or op == "%":
    print(( x/y ) * 100)
elif op == "add" or op == "+":
    print(x+y)
elif op == "subtract" or op == "-":
    print(x-y)
elif op=="multiply" or op == "*":
    print(x*y)
elif op=="division" or op == "/":
    print(x/y)
elif op=="exponent" or op == "**":
    print(x**y)
elif op=="modulus":
    print(x%y)
elif op == "Bitwise And" or op == "&":
    print("Binary for", x, "is", bin(x))
    print("Binary for", y, "is", bin(y))
    print("Answer in binary is", bin(x&y))
    print(x&y)
    
elif op == "Bitwise Or" or op == "|":
    print("Binary for", x, "is", bin(x))
    print("Binary for", y, "is", bin(y))
    print("Answer in binary is", bin(x|y))
    print(x|y)
else:
    print(" Invalid Opperator or Calculator does not support" )
  