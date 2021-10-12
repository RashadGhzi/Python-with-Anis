"""
item = open("anis.txt", "r+")
file = (item.readline())
print(file)
"""
"""
item = open("anis.txt", "r+")
file = item.write("Anisul islam is good boy.")
print(file)
"""

item = open("anis.txt", "r")
file = item.readlines()
for item1 in file:
    print(item1)
item.close()