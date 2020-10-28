def circleOfNumbers(n, firstNumber):
    '''
    Assume numbers [1 ,n] are arranged equally spaced around a circle, find the number
    across from firstNumber
    '''
    return (firstNumber + n//2) % n
