class student():
    roll = ""
    gpa = ""

rahim = student()
print(isinstance(rahim,student))
rahim.roll = 101
rahim.gpa = 3.5
print(f"Rahim roll is {rahim.roll}. \nRahim gpa is {rahim.gpa}\n")

karim = student()
karim.roll = 105
karim.gpa = 5
print(f"Karim roll is {karim.roll}. \nKarim gpa is {karim.gpa}\n")

abdullah = student()
abdullah.roll = 1
abdullah.gpa = 5
print(f"Abdullah roll is {abdullah.roll}. \nAbdullah gpa is {abdullah.gpa}")