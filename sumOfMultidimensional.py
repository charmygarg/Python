def myFunction(myList):
    total =0
    number_of_rows = len(myList)
    number_of_columns = len(myList[0])
    
    rows = 0
    while rows < number_of_rows:
        columns = 0
        
        while columns < number_of_columns:
            total = total + myList[rows][columns]
           
            columns = columns + 1
        rows = rows + 1
    return total