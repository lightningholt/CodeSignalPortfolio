def circleOfNumbers(n, firstNumber):
    '''
    Given a cirlce with n evenly spaace numbers, find the number across from firstNumber
    '''

    # if n % 2 != 0:
    #     half_
    #     half_n = n//2
    half_n = n//2

    opp_number = firstNumber + half_n

    if opp_number >= n:
        opp_number -= n

    return opp_number
