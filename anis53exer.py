class Area():
    base = ""
    height = ""

    def __init__(self,base,height):  # This is constructor file
        self.base = base
        self.height = height

    def triangle_area(self):
        print(f"Area = {0.5*(self.base)*(self.height)}.")

    def rectangle_area(self):
        print(f"Area = {(self.base)*(self.height)}")

t1 = Area(10,20)
t1.triangle_area()

t2 = Area(20,30)
t2.rectangle_area()