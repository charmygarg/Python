def my_function(k):
    my_list = []
    for x in range(1,k):
        if k==1:
            return my_list
        else:
            cube_root = x**(1/3)
            my_list.append(cube_root)
    return my_list.sort()