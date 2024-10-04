
n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    # چاپ فاصله‌ها برای ایجاد وسط‌چین کردن
    print(" " * (n - i), end="")
    # چاپ ستاره‌ها
    print("⭐️" * i)
