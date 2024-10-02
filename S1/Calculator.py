
import math

number = int(input("Please enter your number: "))

print("you choices are: ")
print("- sqrt ( √ ) \n- sin \n- cos \n- tan \n- cot")

operator = input("Please enter your desired operation: ")

if (operator == "sqrt" ):

    number = math.sqrt(number)
    print ("out put is: " ,number)
elif (operator == "sin"):
    
    number = math.radians(number)
    number = math.sin(number)
    print ("out put is : {0}" ,number)
elif (operator == "cos"):
        
    number = math.radians(number)
    number = math.cos(number)
    print ("out put is : {0}" ,number)
elif (operator == "tan"):
        
    number = math.radians(number)
    number = math.tan(number)
    print ("out put is : {0}" ,number)
# elif (operator == "cot"):
        
#     number = math.radians(number)
#     number = math.
#     متاسفانه نتوانستم متد کوتانژانت رو در تابع ریاضی پیدا کنم.
else:
    print("that operation you choice is incorrect.")
    
