cart_value = 0

while True:
    x = int(input("enter price "))
    cart_value = cart_value + x
    print(f"Your total amount is {cart_value}")
    y = input("do u have more items (y/n) ")
    if y == "y":
        continue
    else:
        break