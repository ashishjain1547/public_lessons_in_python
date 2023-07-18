import re 

str_1 = "Hi, my name is Johanth!"
str_2 = "I am 13 years old."
str_3 = "You can reach me at 9876543210."
str_4 = "You can email me at johanthyada@gmail.com"

l = [str_1, str_2, str_3, str_4]

for i in l:
    x = re.search('[0-9]', i)
    if x:
        print(i, ": Found at :", x.span(), ": Found what :", x.group())