def arrayChange(inputArray):
    
    moves = 0
    diff = 0
    
    for i in range(len(inputArray)-1):
        if inputArray[i+1] <= inputArray[i]:
            diff = inputArray[i] - inputArray[i+1] + 1
            inputArray[i+1] += diff
            moves += diff
        
    return moves
