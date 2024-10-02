
b = 1
a = 0
i = 1

print("!!! You must divide the number you want by 2.")
n = int(input("Enter the number: "))
print("---------------------------------------")

print(a)
print(b)

while True:
    if (i<=n):
        c = a+b
        print(c)
        a = b
        b = c
        i = i + 1
    else:
        break

