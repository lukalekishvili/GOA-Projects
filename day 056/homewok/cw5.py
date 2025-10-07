def all_unique_letters(text):
    for letter in text:
        if text.count(letter) > 1:  
            return False             
    return True 