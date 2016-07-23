def my_function(k):
    my_list = []
    divisor = k
    for x in range(1,k+1):
        if divisor % x == 0:
            my_list.append(x)
    return my_list
            