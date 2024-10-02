import random

random_n = random.randint(1,10)
i = 0

while True:
    i = i+1 
    user_n = int(input("Please enter your gess: "))

    if (user_n > random_n):
        print("Try Again! You guessed too small")
    elif (user_n < random_n):
        print("Try Again! You guessed too high")
    else:
        print("Congratulations!")
        break

print("The count number of you gess: ",i)