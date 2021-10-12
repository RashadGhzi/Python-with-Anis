
class student ():
    roll = ""
    gpa = ""

    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def __str__(self):
        return f"Roll : {self.roll}, GPA : {self.gpa}"

    def __eq__(self, other):        # This is equal magic methode
        return self.gpa == other.gpa and self.roll == other.roll

rahim = student(10,5)
print(rahim)

like = student(10,5)
print(like)

print(rahim == like)