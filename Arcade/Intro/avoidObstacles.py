def avoidObstacles(inputArray):
    '''
    Given an array of obstacle positions (inputArray), find the minimum length of jump
    such that all obstacles are avoided.
    '''

    start_pt = 0

    max_pos = max(inputArray)
    pos = 0
    jump = 1
    while pos < max_pos:
        pos += jump

        for i in inputArray:
            if pos == i:
                jump+=1
                pos = 0

    return jump
