
number1 = int(input("PLease Enter your first number: "))
number2 = int(input("PLease Enter your second number: "))


for i in range(number2 , (number1*number2)+1):
    if (number1 % i == 0 and number2 % i == 0 ):

        LCM = i
        break

print("LCM: ", LCM)
