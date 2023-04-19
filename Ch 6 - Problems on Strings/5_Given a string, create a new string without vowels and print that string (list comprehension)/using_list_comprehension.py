x = ['a', 'e', 'i', 'o', 'u']
y = input("please enter the word: ").lower()
result = [i for i in y if i not in x]

print("".join(result))