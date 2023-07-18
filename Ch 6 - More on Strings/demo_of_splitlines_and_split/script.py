with open("myfile.csv", mode = 'r') as f:
    data = f.read()

print(data)
print(type(data)) # <class 'str'>

data = data.splitlines() # Splits the string at line breaks and returns a list

print("List of strings")
print(data)
print(type(data)) # <class 'list'>

# Using list comprehension
# data = [x.split(',') for x in data]

output = []
for i in data:
    output.append(i.split(","))


print("List of list")
print(output)



