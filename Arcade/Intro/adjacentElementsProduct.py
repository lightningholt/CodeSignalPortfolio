def adjacentElementsProduct(inputArray):
    max_prod = -1e10
    adj_prod = 0
    n = len(inputArray)
    
    for i in range(n-1):
        adj_prod = inputArray[i] * inputArray[i+1]
        
        if adj_prod > max_prod:
            max_prod = adj_prod
    
    return max_prod


