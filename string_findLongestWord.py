def find_longest_word(some_string):
    splitted_string = input_string.split()
    maximum_length = len(splitted_string[0]) 
    longest_word = splitted_string[0]
    
    for string in splitted_string:
       
        string_length = len(string)
        if string_length >= maximum_length:
            
            longest_word = string
    return longest_word