
number1 = int(input("PLease Enter your first number: "))
number2 = int(input("PLease Enter your second number: "))

GCD = 1

for i in range(1 , number2+1):
    if (number1 % i == 0 and number2 % i == 0 ):
        GCD = i

print("GCD: ", GCD)