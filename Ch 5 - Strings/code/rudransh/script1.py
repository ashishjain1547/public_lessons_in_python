"""
1. Declare a string variable
2. Print the third letter from that string
3. Print the length of the string variable
"""
#1
name="rudransh"
#2
print(name[2])
#3
print(len(name))

if name == name[::-1]:
    print("It is a palindrome")
else:
    print("Not a palindrome")