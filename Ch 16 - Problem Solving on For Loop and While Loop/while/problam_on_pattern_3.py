"""
1010101
10101 
101  
1   
"""

i = 4

while(i > 0):
    s = "10" * i # Repeating a string using * operator. 
    s = s[:-1]
    print(s)
    i -= 1


"""
i = 4
s = 10101010

[:-1] => Expands to [0 : len() -1]

[:] expands to [0:len()] : End to end
[:-1] expands to [0 : len() - 1] -> end to end except the last element
[:-2] expands to [0 : len() - 2] -> end to end except the last two elements 

"""