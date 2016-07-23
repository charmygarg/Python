def _construct_dictionary_from_file_sample2_(filename):
    my_dictionary = {}
    file_pointer = open(filename, 'r')
    data = file_pointer.readlines()
    for line in data:
        if line[0] != '#':
            name, math, physics, chemistry, biology = line.strip().split(',')
            if float(math) > 70 and float(chemistry) > 70:
                my_dictionary[name] = [float(math), float(physics), float(chemistry), float(biology)]
    return my_dictionary