def addTwoDigits(n):
    '''
    Find the sum of the digits of a number n
    '''
    return sum( int(char) for char in str(n))
