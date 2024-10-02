
name = input("Please enter your name: ")
l_name = input("Please enter your last name: ")
score_f = int(input("Please enter your scoes: \n" ))
score_s = int(input())
score_th = int(input())

course = (score_f + score_s + score_th)/3

if course <= 17:
    print("You are an excellent student.")
elif  17 < course >= 12 :
    print("You are an ordinary student.")
elif course < 12:
    print("You are a condition student.")
