try:
    """
    Turn input into float
    :x: int.
    :return: float
    """
    x = input("Give me something to float ")
    x = float(x)
    print (x)
except ValueError:
    print ("Invalid Input")