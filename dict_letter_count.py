def _dictionary_of_letter_counts_sample_(sample_string):
    stripped_string = sample_string.replace(" ", "")        
    lowercase_stripped_string = stripped_string.lower()     
    sample_dictionary = {}
    
    for character in lowercase_stripped_string:
        sample_dictionary[character] = lowercase_stripped_string.count(character)
    return sample_dictionary