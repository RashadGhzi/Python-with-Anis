#__________________________________MAP Function__________________________________
"""

def square(x):
    return x*x
list1 = [1,2,3,4,5]
n = list(map(square,list1))
print(n)


"""



#__________________________________FILTER Function__________________________________


def num(x):
    return x%2 == 0
num1 = [1,2,3,4,5]

print(list(filter(num,num1)))


