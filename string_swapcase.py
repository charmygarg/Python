def myFunction(myString):
    output = ""
    for i in myString:
        output = i + output
    return output.swapcase()