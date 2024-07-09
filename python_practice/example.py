def squared():
    """
    Squares the number entered by user
    :x: int.
    :print: x**2.
    """
    x = input("Give me something to square ")
    x = int(x)
    print (x**2)

def talk_back():
    """
    Repeats back the input
    :print: x.
    """
    x = input("Wanna play the repeater? ")
    print (x)

def options(a, b, c, d = 2, e = 5):
    """
    Take 3 required and 2 optional parameters
    :print:.
    """
    print (a + b + c)
    print (d + e)
    print (a + b + c + d + e)

squared()
talk_back()
options(5, 6, 7, 1 , 1)