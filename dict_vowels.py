def myFunction(myString):
    stripped_value = myString.replace(" ", "")
    lower_value = stripped_value.lower()
    output = {}
    for i in lower_value:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" :
            output[i] = lower_value.count(i)
    return output