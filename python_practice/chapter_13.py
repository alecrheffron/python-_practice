# Challenge One and Two and Three

class Shape:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return (self.width * 2) + (self.length * 2)

    def change_size(self, change):
        self.change = change
        self.width += change
        self.length += change

    def what_am_i(self):
        if (self.length == self.width) == True:
            print("I'm a square")
        else:
            print("I'm a rectangle")

class Rectangle(Shape):
    pass

class Square(Shape):
    pass

a_square = Square(5, 5)
a_rectangle = Rectangle(5, 4)
a_square.change_size(-.5)


# Challenge Four

class Horse():
    def __init__(self,
                 height,
                 weight,
                 time,
        rider):
        self.height = height
        self.weight = weight
        self.time = time
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name

rider = Rider("Speedy Gonzalez")
horse = Horse(25,
              2140,
              "1:34",
              rider)

