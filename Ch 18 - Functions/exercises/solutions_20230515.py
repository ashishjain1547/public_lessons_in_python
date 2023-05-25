'''1. Divisibility by 13.

2. Check if a number is odd or even.

3. Define a function that takes two integers as input and prints all the even numbers falling in between those two numbers. 

4. Define a function that takes an integer as input and print that many prime numbers starting from 2.

5. Define a function that takes an integer as input and print it's table.'''

x = int(input("enter num "))
def div7():
    if x%13 == 0:
       print("yes,divisible by 13")
    else:
       print("no, not divisible by 13")
div7() 

def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def print_even_numbers(s, e):
    for num in range(s + 1, e):
        if num % 2 == 0:
            print(num)

sn = int(input("enter num "))
en = int(input("enter num "))
print("Even numbers between", sn, "and", en)
print_even_numbers(sn, en)


def table(x):
    for i in range(1,11):
        j = i *x
        print(x,"*",i,"=",j)


x = int(input("enter number: "))
table(x)