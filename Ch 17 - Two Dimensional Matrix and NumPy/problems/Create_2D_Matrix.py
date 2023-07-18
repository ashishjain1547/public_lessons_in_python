r = 3 # Number of rows
c = 3 # Number of columns

mylist = []

cntr = 1

for i in range(r):
    temp = []
    for j in range(c):
        temp.append(cntr)
        cntr += 1
    mylist.append(temp)

print(mylist)