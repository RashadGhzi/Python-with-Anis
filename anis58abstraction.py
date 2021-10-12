# This is abstraction

from abc import ABC,abstractmethod

class shape (ABC):
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight

    @abstractmethod
    def area (self):
        pass

class triangle(shape):
    def area(self):
        result = 0.5 * self.height * self.weight
        print ("The area of triangle is " ,result)

class rectangle(shape):
    def area(self):
        result = self.height * self.weight
        print("The area of rectangle is " ,result)


a = triangle(20,10)
a.area()

b = rectangle(20,10)
b.area()