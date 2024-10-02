hour = int(input("Please enter your hour time: "))
minute = int(input("Please enter your minute time: "))
second = int(input("Please enter your second time: "))

convert = (hour * 3600) + (minute * 60) + second

print("convert that time you say is: ",convert)