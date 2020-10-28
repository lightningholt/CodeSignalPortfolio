def palindromeRearranging(inputString):
    
    counted_chars = []
    pal_counts = []
    
    for i in range(len(inputString)):
        
        if inputString[i] not in counted_chars:
            counted_chars.append(inputString[i])
            char_count = inputString.count(inputString[i])
            
            if char_count % 2 == 0:
                pal_counts.append(0)
            else:
                pal_counts.append(1)
        
    
    
    if sum(pal_counts) <= 1:
        return True
    else:
        return False 
