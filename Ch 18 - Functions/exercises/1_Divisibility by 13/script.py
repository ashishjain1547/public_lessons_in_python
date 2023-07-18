x = int(input("Enter a natural number that you want to see is divisible by 13: "))

def div_by_13(x):
    if x % 13 == 0:
        return True
    else:
        return False 

print(div_by_13(x))