def matrixElementsSum(matrix):
    '''
    Find the sum of all values in matrix not below a 0.
    '''
    cost = 0
    bad_inds = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j not in bad_inds:
                cost += matrix[i][j]
            if matrix[i][j]==0:
                bad_inds.append(j)


    return cost
