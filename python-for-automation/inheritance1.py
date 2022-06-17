#hierarchical inheritance -
class Shape:
    def __init__(self,dm1,dm2): # declaring a constructor
        self.dm1 = dm1
        self.dm2 = dm2

    def area(self):
        print("This is method of Shape class")

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