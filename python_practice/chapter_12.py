# Challenge One
class Apple():
    def __init__(self, c, s, oz, w, h):
        self.color = c
        self.shape = s
        self.ounces = oz
        """measurements in centimeters"""
        self.width = w
        self.height = h

granny_smith = Apple("light green", "round", 15, 20, 20)
print(granny_smith.color)

# Challenge Two

import math

class Circle:
    def __init__(self, r):
        """ centimeters """
        self.radius = r

    def area(self):
        return self.radius * self.radius * math.pi

circle = Circle(12)
print(circle.area())

# Challenge Three

class Triangle:
    def __init__(self, b, h):
        """ Height in centimeters """
        self.base = b
        self.height = h

    def area(self):
        return (self.base * self.height) / 2

triangle = Triangle(15, 20)
print(triangle.area())

# Challenge Four

class Hexagon:
    def __init__(self, s):
        self.side = s

    def perimeter(self):
        return self.side * 6

hexagon = Hexagon(5)
print(hexagon.perimeter())