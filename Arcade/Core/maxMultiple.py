def maxMultiple(divisor, bound):
    '''
    Find the greatest number [0, bound] evenly divisible by divisor
    '''
    return max([x for x in range(bound+1) if x % divisor == 0])
