
# 1 + 2 + 3 + .... n
# 2 + 4 + 6 + .... n
# 1 + 4 + 7 + .... n
# 1*1 + 2*2 + 3*3 + .... n
# 2*2 + 4*4 + 6*6 .... n
# 1*1 + 4*4 + 7*7 + .... n


## 1
"""print("1 + 2 + 3 + .... n.")
n = int(input("Enter the last number for summation:"))
sum = 0
for item in range(1,n+1,1):
    #print(item)
    sum = sum + item
print(sum)"""


##2
"""print("2 + 4 + 6 + .... n.")
print("Enter the last number for summation:")
sum = 0
n = int(input())
for item in range(2,n+1,2):
    sum = sum + item
print(sum)"""


##3
"""print("1 + 4 + 7 + .... n.")
print("Enter the last number for summation:")
sum = 0
n = int(input())
for a in range(1,n+1,3):
    sum = sum + a
print(sum)"""


##4
"""print("1*1 + 2*2 + 3*3 + .... n.")
print("Enter the last number:")
n = int(input())
sum = 0
for item in range(1,n+1,1):
    sum = sum + item*item
print(sum)
"""

##5
"""
print("2*2 + 4*4 + 6*6 .... n.")
print("Enter the last number:")
n = int(input())
sum = 0
for item in range(2,(n+1),2):
    sum = sum + (item*item)
print(sum)
"""


##6
"""
print("1*1 + 4*4 + 7*7 + .... n.")
print("Enter the last number:")
n = int(input())
sum = 0
for number in range(1,(n+1),3):
    sum = sum + (number*number)
print(sum)
"""