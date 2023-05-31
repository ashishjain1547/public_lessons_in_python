def div7(x):
    if x % 7 == 0:
        print("yes, it is divisible")
    else:
        print("no, not divisible")


# Check if a number is prime or not.

x = int(input("enter a number "))
def prime(x):
    for i in range(2,x):
      if x%i == 0:
         msg = "it is not a prime number "
         break
      else:
         msg = "yes it is a prime number "  
    print(msg)
prime(x)