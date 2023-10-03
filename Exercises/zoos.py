name=input()

var_z=0
var_o=0

var_z = name.count("z")
var_o = name.count("o")

if var_o == 2 * var_z:
    print("Yes")
else:
    print("No")