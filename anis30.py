
num = input("Enter  the numbers you want to summtion of :\n" )
list = num.split()
sum = 0
for item in list:
    sum = sum + int(item)
print(sum)