# List comprehensions
num = [1,2,3,4,5]
result = [x*x for x in num]
print(result)

result1 = [x for x in num if x%2 == 0]
print(result1)