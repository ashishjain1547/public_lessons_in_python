participants = ['   Ashish     ', '        Sonia            ', ' Johanth'] # A list of strings

for i in participants:
    print(i.strip())


for i in participants:
    print(len(i))
    temp = i.strip()
    temp = temp.zfill(20)

    print(temp)
    print(len(temp))
    print("")

