x = ['a', 'e', 'i', 'o', 'u']
y = input("please enter the word: ").lower()

result=""

for i in range(len(y)):
    if y[i] not in x:
        result = result + y[i]
    else:
        print(y[i])

print("After Removing Vowels: ", result)
