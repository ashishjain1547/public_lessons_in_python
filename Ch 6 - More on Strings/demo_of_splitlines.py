data = """My name is Ashish.
I come from Delhi.
I love programming.""" # Multiline Strings

print(data)
print(type(data)) # type of data

d = data.splitlines() # Breaks your string at line breaks and returns a list of strings.

print(d)
print(type(d))

# Can we do the reverse of spltlines?

temp = "\n".join(d) # We are processing a list this time.
print(temp)

