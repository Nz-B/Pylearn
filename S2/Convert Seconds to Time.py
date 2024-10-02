
user_second = int(input("Please enter your seconds time: "))

hour = user_second // 3600
if ( user_second % 3600 > 60 ):
    minuet = (user_second %3600) / 60
else:
    minuet = 0
 
if ( user_second % 3600 < 60 ):
    second = (user_second % 3600)


print(f"{hour:02}:{minuet:02}:{second:02}")