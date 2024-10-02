
weight = float(input("Please enter your weight in kilograms: "))
height = float(input("Please enter your weight in meters: "))

BMI = (weight/(height**2))*10000
print(BMI)

if ( 35<= BMI <= 39.9 ):
    print("You in exterme obesity level")
elif ( 30<= BMI <= 34.9 ):
    print("You in obesity level")
elif ( 25<= BMI <=29.9 ):
    print("You in overweight level")
elif ( 18<= BMI <= 24.9):
    print("You in normal weight level")
else :
    print("You in undeweight level")
