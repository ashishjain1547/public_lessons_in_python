#Check if given String is Pangram or not
x = "abcdefghijklmnopqrstuvwxyz"
y = input("please enter the sentence: ").lower()
f = open("pang.txt", "w")
for i in x:
    if i in y:
        print(i,"=","yes")
        b="y"
        f = open("pang.txt", "a")
        f.write(b)
        f.close()
    else:
        print(i,"=","no")
        h="n"
        f = open("pang.txt", "a")
        f.write(h)
        f.close()

with open('pang.txt', 'r') as file:
    data = file.read()
    string_length = len(data)
    print(f"The length of the string in the file is: {string_length}")
    print("Data in file: ", data)
    p=data.count("y")
    t=data.count("n")
    print("Count of Yes:", p)
    print("Count of No:", t)
if t == 0:
    print("ya! This sentence is a pangram :)")
else:
    print("no! This sentence is not a pangram :(")
 

    



