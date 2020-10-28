def allLongestStrings(inputArray):
    '''
    Given an array of strings, find all the longest strings
    '''
    longest = 0
    long_array = []

    for i in inputArray:
        if len(i) > longest:
            long_array = [i]
            longest = len(i)
        elif len(i) == longest:
            long_array.append(i)
        else:
            continue

    return long_array
