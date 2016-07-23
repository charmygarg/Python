def my_function(vector):
    x = vector[0]
    y = vector[1]
    z = vector[2]
    mag = ((x**2) + (y**2) + (z**2)) ** (1/2)
    x1 = x/mag
    y1 = y/mag
    z1 = z/mag
    unit_vector = [x1, y1, z1]
    return(unit_vector)
    