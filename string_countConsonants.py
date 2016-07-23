# Type your code here
def count_consonants(some_string):
    spaceRemove = some_string.replace(" ", "")
    count = 0
    vowels =['a' , 'e' , 'i' , 'o' , 'u]
    for i in spaceRemove.lower():
        if i not in vowels :
            count = count + 1
    return count