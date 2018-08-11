# Polygon Example w/ Triangle and Rectangle subclasses

from math import pi

class Polygon:
    def __init__(self, num_sides):
        self.n = num_sides
        self.sides = [int(input("Enter side " + str(i+1) + " : ")) for i in range(self.n)]

    def display_side(self):
        for i in range(self.n):
            print("Side", i+1, "is", self.sides[i])

    def __str__(self):
        return "Polygon with " + str(self.n) + " sides: " + str(self.sides)

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def print_area_tri(self):
        a, b, c = self.sides
        # Calculate the semi-perimeter
        s = (a + b + c)/2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print("The area of the triangle is %0.2f" %area)

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)

    def print_area_rect(self):
        a, b = self.sides
        # Calculate area of rectangle
        area = a * b
        print("The are of the rectangle is %0.2f" %area)

class Circle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 1)

    def print_area_cir(self):
        a = self.sides[0] # Input is a list
        # Calculate area of circle
        radius = a / (pi * 2)
        area = pi * radius ** 2
        print("The area of the circle is %0.2f" %area)


#Testing the polygon class
p = Polygon(8)
print(p)
#Testing the triangle class
t = Triangle()
t.print_area_tri()
#Testing the rectangle class
r = Rectangle()
r.print_area_rect()
#Testing the rectangle class
c = Circle()
c.print_area_cir()
