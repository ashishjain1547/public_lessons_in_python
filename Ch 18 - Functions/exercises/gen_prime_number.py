# 4. Define a function that takes an integer as input and print that many prime numbers starting from 2.

import math

x = int(input("Enter the number of primes that you want: "))

from math import factorial

def is_prime(x):
    if x == 0 or x == 1:
        return False 

    for i in range(2, x):
        if x % i == 0:
            return False
        else:
            continue
    return True


def generate_prime(num_primes):
    l = []

    next = 2
    
    while True:
        if is_prime(next) and len(l) < num_primes:
            l.append(next)
        else:
            if len(l) >= num_primes:
                break
        next = next + 1
    return l

l = generate_prime(x)
print(l)
