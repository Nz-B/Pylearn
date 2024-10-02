while True:

    number1 = int(input("Please enter your number: "))
    number2 = int(input("Please enter your number: "))

    print("you choices are: ")
    print("1. + \n2. - \n3. * \n4. / \n5. % \n6. exit ")

    operator = input("Please enter your desired operation: ")

    if (operator == "+" ):

        number_t = number1 + number2
        print ("out put is: " ,number_t)
    elif (operator == "-"):
        
        number_t = number1 - number2
        print ("out put is: " ,number_t)
    elif (operator == "*"):
            
        number_t = number1 * number2
        print ("out put is: " ,number_t)
    elif (operator == "/"):
            
        number_t = number1 / number2
        print ("out put is: " ,number_t)
    elif (operator == "%"):

        number_t = number1 % number2
        print ("out put is: " ,number_t)
    elif (operator == "exit"):
        break
    else:
        print("that operation you choice is incorrect.")
    