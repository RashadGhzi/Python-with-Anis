"""# This is multilevel inheritence.
class A ():
    def display1 (self):
        print("I am in class A.")

class B (A):
    def display2 (self):
        print("I am in class B.")

class C (B):
    def display3 (self):
        super().display1()
        super().display2()
        print("I am in class C.")

item = C()
item.display3()
"""


# This is multiple inheritence
class A ():
    def display(self):
        print("I am in class A.")

class B ():
    def display(self):
        print("I am in class B.")

class C(A,B):
    pass

item = C()
item.display()
