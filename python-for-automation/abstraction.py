# Abstraction-
from abc import ABC,abstractmethod # common line for using abstraction
class Shape(ABC): # ABC will prefer in parameter in parent class during abstraction

    def __init__(self,dm1,dm2): # declaring a constructor
        self.dm1 = dm1
        self.dm2 = dm2

    @abstractmethod # must be kept this line- @abstractmethod
    def area(self):
        pass # keeping the method without any body is actually abstraction

class Triangle(Shape):
    def area(self): #overiding
        area = 0.5 * self.dm1 * self.dm2
        print("Area of Triangle :  " , area)


class Rectangle(Shape):
    def area(self): #overiding
        area = self.dm1 * self.dm2
        print("Area of Rectangle :  " , area)


t1 = Triangle(20,40)
t1.area()

r1 = Rectangle(4,5)
r1.area()