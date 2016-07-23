import numpy
def myFunction(my_tuple):
    mean = sum(my_tuple)/len(my_tuple)
    median = numpy.median(numpy.array(my_tuple))
    return mean, median