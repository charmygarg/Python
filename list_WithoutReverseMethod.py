def myFunction(input_list):
    output_list = []
    newList = input_list[:]
    myList = len(newList)
    for x in range(myList-1,-1,-1):
        output_list.append(newList[x])
    return output_list
        