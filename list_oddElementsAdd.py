def myFunction(myList):
    input_list = myList[:]
    for i in range(0,len(input_list)):
        if input_list[i]%2 !=0:
            input_list[i] = input_list[i] + 1  
    return input_list    
        
            