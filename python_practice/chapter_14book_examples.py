
class Rectangle():
# Class Variable
    recs = []

    def __init__(self, w, l):
# Instance variables
        self.width = w
        self.length = l
        self.recs.append((self.width,
                          self.length))

    def print_size(self):
        print("""{} by {}
              """.format(self.width,
                         self.length))

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs[1])

# Modifying print magic method

class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

lion = Lion("Dilbert")
print(lion)

class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        # abs makes it an absolute value, meaning it will aways return the positive version of the number
        return abs(self.n +
                   other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)

# 'Is' keyword, will return a boolean respose
class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)

# Use the 'is' keyword to check if a variable is none

def x_is_none(x):
    if x is None:
        print("x is None :( ")
    else:
        print("x is not None")

x = 10
x_is_none(x)
x = None
x_is_none(x)
