"""
(1) Write a function named insert that accepts a sorted list L of integers and an integer x as arguments. It should return a sorted list with the element x inserted into the input list at the right place.

(2) Write a recursive function named isort that accepts a non-empty list L of integers as argument. It should return a sorted list in ascending order. isort must make use of insert. This is a popular sorting algorithm and is called insertion sort.

(1) Each test case corresponds to one function call.

(2) You do not have to accept input from the user or print the output to the console. You just have to write the definition of both the functions.

(3) You cannot use any built-in sort functions or methods in this problem.
"""

def insert(L, x):
    ix = -1
    for i in range(len(L)):
        if x <= L[i]:
            ix = i 
            break

    if ix != -1: 
        m = L[:ix] + [x] + L[ix:]
    else:
        m = L + [x]
    return m 

def isort(L):
    
    if len(L) > 1:
        L2 = isort(L[:len(L)-1])
        L2 = insert(L2,L[-1])

    else:
        L2 = L 

    return L2 


l = [65, 7, 33, 78, 10, 100]
m = isort(l)
print(m)

l = [5, 65, 7, 33, 78, 10]
m = isort(l)
print(m)