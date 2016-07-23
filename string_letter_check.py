def myFunction(myString , myChar):
    count = 0
    for i in myString.upper():
        if i in myChar.upper():
            count = count + 1
    return count