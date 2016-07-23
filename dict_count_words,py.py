def myFunction(myString):
    output = {}
    lower_value = myString.lower()
    splitted_value = lower_value.split()
    
    for i in splitted_value:
        output[i] = splitted_value.count(i)
    return output