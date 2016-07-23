def myFunction(inputString):    
    count = 0
    myString = inputString.upper().split()
    for i in myString:
        if len(i) > 4:    
            count = count + 1
    return count