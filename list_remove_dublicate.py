def myFunction(myList):
    newList = []
    for i in myList:
        if i not in newList:
            newList.append(i)
    return newList