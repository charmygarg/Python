def myFunction(input_string):
    output_string = ""
    for i in input_string:
        output_string = i + output_string
    if input_string.upper() == output_string.upper():
        return True
    else:
        return False