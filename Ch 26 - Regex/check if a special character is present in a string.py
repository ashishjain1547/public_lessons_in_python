"""Q: I want to find if a special character from (, ! ? . + @) is present in a string.
A: """
import re 

str_1 = "Hi, my name is Johanth! Nice to meet you."
str_2 = "I am 13 years old. And you?"
str_3 = "You can reach me at +91 9876543210."
str_4 = "You can email me at johanthyada@gmail.com"

l = [str_1, str_2, str_3, str_4]

for x in l:
    y = re.search("[!?+@]", x)
    if y:
        print(x)
        print("Found at :", y.span(), ": Found what :", y.group())