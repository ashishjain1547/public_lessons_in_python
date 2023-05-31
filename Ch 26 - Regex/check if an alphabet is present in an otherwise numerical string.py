import re 
import random 
import string
 
# Randomly choose a letter from all the ascii_letters

l = []
for i in range(20):
    x = [str(random.randint(0,9)) for j in range(10)]
    x[random.randint(0,9)] = random.choice(string.ascii_letters)

    l.append(''.join(x))

print(l)


"""
Homework:

Find the alphabets in a list of numerical strings using Regex.

['496d665979', '772T202957', '23650784J3', '4252925k32', '72733Q8098', '464W826820', '5990A42505', '4725V73478', '77148363L1', '3W15107781', 'Q088253588', '2660g58899', '81719893v3', '35s1605748', '442139N477', 'O724424959', '4E06284727', '160804Q000', '8726r38255', '1b38353340']
"""

for i in l:
    x = re.search('[a-zA-Z]', i)
    if x:
        print(i, ": Found at :", x.span(), ": Found what :", x.group())