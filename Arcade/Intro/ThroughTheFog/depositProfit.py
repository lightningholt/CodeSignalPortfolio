def depositProfit(deposit, rate, threshold):
    
    year = 0
    while deposit < threshold:
        year += 1
        deposit *= 1+(0.01*rate)
        
    
    return year


