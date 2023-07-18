# 4. Define a function that takes an integer as input and print that many prime numbers starting from 2.

import math

x = int(input("Enter the number of primes that you want: "))


from math import factorial

def is_prime(x):
    return factorial(x - 1)  % x == x - 1



def generate_prime(num_primes):
    l = []

    next = 2
    while len(l) < num_primes:
        if len(l) == 0:        
            l.append(next)
            continue
        else:
            next = l[-1]

        next = next + 1
        if is_prime(next):
            l.append(next)
        
    return l


l = generate_prime(x)
print(l)