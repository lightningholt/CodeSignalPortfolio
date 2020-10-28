def phoneCall(min1, min2_10, min11, s):
    '''
    You have s cents. The first minute of a phone call costs min1, minutes 2-10
    cost min2_10, and every minute beyond that costs min11. Find the greatest
    length of phone call you can make.
    '''
    if s - min1 < 0:
        return 0
    elif s - min1 - 9*min2_10 > 0:
        return 10 + (s-min1 - min2_10 * 9)//min11
    else:
        return 1 + (s-min1)//min2_10
