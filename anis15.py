
a = 100000
b = 50000000
c = 90000000

if a > b:
    if a > c:
        print(a)
    else:
        print(c)

elif b > a:
    if b > c:
        print(b)
    else:
        print(c)

else:
    print(c)