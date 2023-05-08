import math

n = 48
quo = math.floor(n/7) # int() was not explicit that we needed a floor value.

if quo*7 == n:
    print("Divisible")
else:
    print("Not Divisible")
