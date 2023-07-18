x = "A line about Python String from the book 'Pg 191, Learning Python (O'Reilly, 5e)': Strictly speaking, Python strings are categorized as immutable sequences, meaning that the characters they contain have a left-to-right positional order and that they cannot be changed in place. In fact, strings are the first representative of the larger class of objects called sequences that we will study here. Pay special attention to the sequence operations introduced in this post, because they will work the same on other sequence types we’ll explore later, such as lists and tuples. Note: All string methods returns new values. They do not change the original string."

print(x.count("a")) # 66
print(x.count("of")) # 7

y = "ashishjain1547@gmail.com"
print("Is this a gmail ID?")
print(y.endswith("gmail.com"))

z = "+91 7696499407"
a = "+1 455 766 8888"
print("Is this number from India?")
print(z.startswith("+91"))
print(a.startswith("+91"))

first_name = 'Ashish'
print("High level validation: Is the first name entered a valid name?")
print(first_name.isalpha())


