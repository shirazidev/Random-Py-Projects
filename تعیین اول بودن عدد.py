def is_prime(x):
    c = 0
    for i in range(1, x):
        if x % i == 0:
            c += 1
    if c == 1:
        return True
    else:
        return False

# دریافت ورودی از کاربر
x = int(input("Enter a number: "))

# بررسی عدد و چاپ نتیجه
if is_prime(x):
    print("prime")
else:
    print("not prime")