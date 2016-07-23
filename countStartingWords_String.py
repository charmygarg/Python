def myFunction(myString, myChar):
    count = 0
    split_string = myString.upper().split()
    for i in split_string:
        if i[0] == myChar.upper():
            count = count + 1
    return count
   