# Challenge One

class Square:
    square_list = []

    def __init__(self, side):
        self.side = side
        self.square_list.append(self.side)

        # Challenge Two
        print("""{} by {} by {} by {}""".format(self.side,
                                                self.side,
                                                self.side,
                                                self.side))

    # Challenge Three
    def we_the_same(x, y):
        if x is y:
            print("You are I")
        else:
            print("I've never seen that object before in my life")


square1 = Square(4)
square2 = Square(7.4)
square3 = Square(4)
print(Square.square_list)

square_one = square1
Square.we_the_same(square1, Square.square_list[0])
Square.we_the_same(square1, square_one)