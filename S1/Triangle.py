
side1 = int(input("Please enter the name of side1: "))
side2 = int(input("Please enter the name of side2: "))
side3 = int(input("Please enter the name of side3: "))

if (side1+side2>side3 and side1+side3>side2 and side2+side3>side1):
    print("Numbers you said are can be triangle.")
else:
    print("Numbers are you said can`t be triangle.")
