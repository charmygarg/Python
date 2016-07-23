from math import *
def my_function(a, b):
    x1 = a[0]
    y1 = a[1]
    z1 = a[2]
    x2 = b[0]
    y2 = b[1]
    z2 = b[2]
    distance = sqrt(((x2 - x1)**2) + ((y2 - y1)**2) + ((z2 - z1)**2))
    return distance