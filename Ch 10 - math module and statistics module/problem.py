""" Intialize a list with any 10 natural numbers and find:
1. Maximum value
2. Minimum value
3. Sum of these 10 numbers
4. Average of these 10 numbers
"""

mylist=[i for i in range(0,10)]
print(mylist)
print(max(mylist), min(mylist), sum(mylist), sum(mylist)/len(mylist))



import random
l = [random.randint(0, 100) for i in range(0, 10)]
print(l)
print(max(mylist), min(mylist), sum(mylist))

import statistics
print("Mean: ", statistics.mean(l))
print("Median: ", statistics.median(l))
print("Mode: ", statistics.mode(l))
print("Stdev: ", statistics.stdev(l))
print("Variance: ", statistics.variance(l))

