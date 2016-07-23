def myFunction(myDict , inputValue):
    output_list=[]
    keys = myDict.keys()
    for i  in keys:
        myList = myDict[i]
        one , two , three = myList[0] , myList[1] , myList[2]
        if one == inputValue or two == inputValue or three == inputValue:
            output_list.append(i)
            output_list.sort()
    return output_list