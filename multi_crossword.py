def _find_word_horizontal(crosswords,word):
    if not crosswords or not word : # if empty then return None
        return None
    for index,row in enumerate(crosswords):
        temp_str=''.join(row)
        if temp_str.find(word)>=0:
            return [index,temp_str.find(word)]
    return None