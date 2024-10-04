
score_number = int(input("Please enter the number of your scors: "))

average = 0

for i in range(score_number):
    score = int(input("Enter the grade: "))
    average = score + average

print("average: ",average/score_number)