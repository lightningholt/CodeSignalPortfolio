def arrayMaximalAdjacentDifference(inputArray):
    '''
    Find the max absolute difference between elements in an array.
    '''
    max_diff = 0

    for i in range(len(inputArray)-1):
        if abs(inputArray[i+1] - inputArray[i]) > max_diff:
            max_diff = abs(inputArray[i+1] - inputArray[i])

    return max_diff
