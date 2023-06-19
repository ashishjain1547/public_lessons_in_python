speed = float(input("Enter the speed of the car: "))

if speed > 70:
    print("High speed vehicle detected.")
elif speed <= 70 and speed >= 40:
    pass 
elif speed < 40:
    print("Very slow moving vehicle detected.")

    