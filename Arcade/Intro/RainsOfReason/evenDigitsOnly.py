def evenDigitsOnly(n):
    '''
    Check if all digits in n are even
    '''
    power = 0
    tens = 0
    m = n 
    while 10**power <= n:
        
        m = m // (10**tens)
        print(m, power)
        
        if m % 2 > 0:
            return False
            break
        
        power += 1
        tens = 1
    
    return True
        


