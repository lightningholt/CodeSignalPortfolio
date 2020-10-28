def knapsackLight(value1, weight1, value2, weight2, maxW):
    '''
    maximize the value in your knapsack. You can only carry maxW,
    and the value and weight of object 1/2 is given by value1/2 and weight1/2
    '''
    if maxW >= weight1 + weight2:
        return value1 + value2
    elif weight1 > maxW and weight2 > maxW:
        return 0
    elif weight2 > maxW:
        return value1
    elif weight1 > maxW:
        return value2
    else:
        return max(value1, value2)
