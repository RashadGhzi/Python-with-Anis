class student ():
    roll = ""
    gpa = ""

    def point(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")

rahim = student()
rahim.point(101,3.5)
rahim.display()