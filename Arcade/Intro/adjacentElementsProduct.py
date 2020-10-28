def adjacentElementsProduct(inputArray):
    # find the greatest product of adjacent elements in inputArray
    max_prod = -1e10 # to catch negative numbers
    adj_prod = 0
    n = len(inputArray)

    for i in range(n-1):
        adj_prod = inputArray[i] * inputArray[i+1]

        if adj_prod > max_prod:
            max_prod = adj_prod

    return max_prod
