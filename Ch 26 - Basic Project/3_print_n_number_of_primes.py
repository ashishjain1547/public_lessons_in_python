instructions = """
1. Take an integer as an input from the user in a variable called x.

2. Define a function isPrime() that tells if the number is prime.

3. Write a function that runs a for-loop for range(0,20) to print the primes from this range as a test.

4. Generate x number of primes.

One interesting point:
Is 1 a prime number yes or no?
For a number to be called as a prime number, it must have only two positive factors. Now, for 1, the number of positive divisors or factors is only one i.e. 1 itself. So, number one is not a prime number.
"""
x = int(input("Enter the number of primes you want:"))

def isPrime(input):
    ret = False
    for i in range(2, input):
        if input % i == 0:
            return ret 
        else:
            ret = True
        
    return ret 

# This is to test isPrime()
def testPrime():
    for i in range(20):
        if isPrime(i):
            print(i)

# testPrime()

c = 2
l = []
while len(l)<x :
     if isPrime(c):
         l.append(c)
     c+=1
print(l)



