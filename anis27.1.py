
# 1 x 2 x 3 x .... n. (Factorial (n!))
# 2 x 4 x 5 x .... n.
# 1 x 3 x 7 x .... n.

print("Enter the number you want to factorial of :")
n = int(input())
m = 1
for x in range(1,(n+1),1):
    m = m * x
print(m)