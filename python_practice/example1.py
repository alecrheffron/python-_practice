def halved():
    """
    Divide by two
    :n: int.
    :return: input / 2.
    """
    n = input("Give me a numba ")
    n = int(n)
    return n / 2

def quaded(x):
    """
    Takes previous modified input and multiply by 4.
    :print: previous function times 4.
    """
    print (x * 4)

x = halved()
quaded(x)