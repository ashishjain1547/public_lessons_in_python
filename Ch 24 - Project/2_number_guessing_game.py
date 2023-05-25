"""
Instructions:
1. Initialize a random number between 0 - 100.
Hint: Use random.randint()

2. Print "I have picked a number between 0 to 100. Your turn to guess it..."

3. Initialize a counter variable to 0 to keep track of number of tries.

4. Start an infinite while loop.

5. Inside loop: take a guess from user. Tell the user number of guesses s/he has made then help him to reach the number through hints like 'Try higher' or 'Try lower'.

"""

import random
x = random.randint(0,100)
print("I have picked a random number beetween 0 to 100 you have ")
c = 0
while True:
     y = int(input("Enter your guess: "))
     c = c+1 
     print(f"u have tried {c} number of times ") 
     if y == x:
        print("Yes u are right")
        break
     else:
        print("no try again")
        if y > x:
            print("Try lower ")
        else:
            print("Try higher")
        continue
