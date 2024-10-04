import time
count = int(input("Enter the number of seconds for the countdown: "))
print("----------------------------------------------------")

i = 0

while (i <= count):
    print(count,"seconds remaining...")
    count -= 1 
    time.sleep(1)
    if count == 0:
        print("Time's up!")
        break
