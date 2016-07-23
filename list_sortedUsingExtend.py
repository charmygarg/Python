def _merge_and_sort_sample_(a, b):
    a.extend(b)
    new_list = []
    while a:
        maximum = a[0]
        for element in a:
            if element > maximum:
                maximum = element
        new_list.append(maximum)
        a.remove(maximum)
    return new_list