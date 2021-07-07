"""  # (X) arguments
def detail1(age, name):
    print(age,name)

detail1(20,"Rashad")
"""


# also (x) arguments
"""def item(*details):
    print(details)

item("age",201,"num","num2")
item(210,510)"""


# (x) arguments
"""def num(*numbers):
    sum = 0
    for item in numbers:
        sum = sum + item
    print(sum)
num(10,20)
num(30,20,50) 
num(10,20,30,40)"""


# (xx) arguments
def item (**details):
    print(details["name"])
item(age = 21, name = "Rashad")