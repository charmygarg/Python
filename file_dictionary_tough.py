def _construct_nested_dictionary_from_file_sample_(filename):
    my_dictionary = {}
    file_pointer = open(filename, 'r')
    data = file_pointer.readlines()
    for line in data:
        if line[0] != "#":
            first_name, last_name, age = line.strip().split(',')
            if last_name not in my_dictionary:
                my_dictionary[last_name] = {first_name: int(age)}
            else:
                if first_name not in my_dictionary[last_name]:
                    my_dictionary[last_name][first_name] = int(age)

    return my_dictionary