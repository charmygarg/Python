def myFunction(input_string):
    vowels = ["A","E","I","O","U"]
    count =0
    for i in input_string.upper():
        if i in vowels:
            count = count + 1
    return count