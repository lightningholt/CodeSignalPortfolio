def mexFunction(s, upperBound):
    '''
    Find a version of the minimum excludant. Given a set s, and an upper bound,
    find the minimum non-negative integer that is not in s and less than or
    equal to the upper bound
    '''
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        if found > upperBound:
            found=upperBound
        elif found == -1:
            found = upperBound

    return found
