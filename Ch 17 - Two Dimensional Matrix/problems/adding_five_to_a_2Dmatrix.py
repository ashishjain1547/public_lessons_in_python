from operator import mod


arr = [ [1, 2, 3],
[4, 5, 6],
[7, 8, 9] ]

for i in arr:
    for j in i:
        print(j + 5)



print("Further if we want to create a new array")

mod_arr = []
for i in arr:
    templist = []
    for j in i:
        templist.append(j+5)
    mod_arr.append(templist)

print(mod_arr)