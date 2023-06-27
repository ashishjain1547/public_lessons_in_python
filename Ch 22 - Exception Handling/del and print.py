# Deleting the entire list using del keyword

thislist = ["apple", "banana", "cherry"]
del thislist

try:
    print(thislist) # Trying to diplay deleted list contents
except Exception as e:
    print(e)