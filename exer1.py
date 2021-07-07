'''
print("How many star pattern do you want?")
m = int(input())
for star in range(1,(m+1),1):
    print(star*("*"))

print("How many reverse star pattern do you want?")
n = int(input())
for i in range(1,(n+1),1):
    num = (n+1)
    num = num - i
    print(num*("*"))
'''
print("How many star patter you wan?")
a = int(input())
num = a
num1 = a
for star1 in range(1,(a+1)):
    num = num-1
    b = "*"
    print(num*" ",b*star1)
for star2 in range(0,a):
    d = "*"
    print(star2*" ",num1*d)
    num1 = num1 - 1
