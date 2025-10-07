def even_first(lst):
    evens = []  
    odds = []   
    for number in lst:      
        if number % 2 == 0:  
            evens.append(number)  
        else:                 
            odds.append(number)   

    return evens + odds