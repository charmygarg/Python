def myFunction(filename):
    my_dict={}
    my_file=open(filename,'r')
    my_str=my_file.readlines()
    for data in my_str:
        names, course1, course2, course3, course4 = data.strip().split(',')
        my_dict[names]=[float(course1), float(course2), float(course3), float(course4)]
    return my_dict