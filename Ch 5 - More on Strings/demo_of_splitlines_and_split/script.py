with open("myfile.csv", mode = 'r') as f:
    data = f.read()

print(data)
print(type(data)) # <class 'str'>

data = data.splitlines() # Splits the string at line breaks and returns a list

print(data)

# Using list comprehension
# data = [x.split(',') for x in data]


output = []
for i in data:
    output.append(i.split(","))

print(output)



