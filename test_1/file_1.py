from datetime import datetime as dt

def time():
    return dt.now()

def sum(*args):
    """
    This function inputs a list of numbers and returns their sum
    """
    args = list(args)
    su = 0
    for i in args:
        su += i
    # su = a + b
    return su

def avg(*args):
    """
    This function inputs a list of numbers and returns their average
    """
    args = list(args)
    su = 0
    co = 0
    for i in args:
        su += i
        co += 1
    su /= co
    return su