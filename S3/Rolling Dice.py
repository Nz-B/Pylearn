import random

sum = 0

while True :
    dic1 = random.randint(1,6)
    dic2 = random.randint(1,6)

    sum = dic1 + dic2

    print("Rolling the dice...")
    print(f"You rolled a {dic1} and a {dic2}. Sum: {sum}")
    print("----------------------------------------------------")

    if (sum == 12):
        print("Congratulations!")
        break

