def myFunction(words):
    word = []
    for i in words:
        word.append(i)
    words.sort()
    if words == word:
        return True
    else:
        return False
    
        