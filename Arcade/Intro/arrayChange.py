def arrayChange(inputArray):
    '''
    Find the minimal number of one-step increases such that inputArray is
    strictly increasing, i.e. inputArray[i] < inputArray[i+1] for all i.
    '''
    moves = 0
    diff = 0

    for i in range(len(inputArray)-1):
        if inputArray[i+1] <= inputArray[i]:
            diff = inputArray[i] - inputArray[i+1] + 1
            inputArray[i+1] += diff
            moves += diff

    return moves
