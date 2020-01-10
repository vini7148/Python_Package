from datetime import datetime as dt

def time():
    return dt.now()

def sum(a, b):
    su = a + b
    return su

def avg(a, b):
    su = sum(a, b)
    su = su / 2
    return su