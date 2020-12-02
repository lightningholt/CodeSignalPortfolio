import numpy as np

def minesweeper(matrix):
    '''
    This implements the game of minesweeper, but not how I'd like it to be.
    For instance, returns a number on the mines, and counts corners or
    something. But that was what codesignal wanted.
    '''

    x = len(matrix)
    y = len(matrix[0])

    counter = np.zeros((x,y))
    matrix = np.array(matrix)
    for i in range(x):
        for j in range(y):
            if i == 0:
                if j == 0:
                    counter[i,j] = np.sum(matrix[i:i+2, j:j+2] * 1) - matrix[i,j]*1
                elif j == y-1:
                    counter[i,j] = np.sum(matrix[i:i+2,j-1:j+1] * 1) - matrix[i,j]*1
                else:
                    # counter[i,j] = matrix[i][j]*1 + matrix[i+1,j]*1 + matrix[i][j+1]*1 + matrix[i][j-1]*1
                    counter[i,j] = np.sum(matrix[i:i+2,j-1:j+2] * 1) - matrix[i,j]*1
            elif i == x-1:
                if j == 0:
                    counter[i,j] = np.sum(matrix[i-1:i+1,j:j+2] * 1) - matrix[i,j]*1
                elif j == y-1:
                    print(np.sum(matrix[i-1:i+1,j-1:j+1] * 1))
                    counter[i,j] = np.sum(matrix[i-1:i+1,j-1:j+1] * 1) - matrix[i,j]*1
                else:
                    # counter[i,j] = matrix[i,j]*1 + matrix[i+1,j]*1 + matrix[i,j+1]*1 + matrix[i,j-1]*1
                    counter[i,j] = np.sum(matrix[i-1:i+1,j-1:j+2] * 1) - matrix[i,j]*1
            else:
                if j == 0:
                    counter[i,j] = np.sum(matrix[i-1:i+2,j:j+2] * 1) - matrix[i,j]*1
                elif j == y-1:
                    counter[i,j] = np.sum(matrix[i-1:i+2,j-1:j+1] * 1) - matrix[i,j]*1
                else:
                    # counter[i,j] = matrix[i,j]*1 + matrix[i+1,j]*1 + matrix[i,j+1]*1 + matrix[i,j-1]*1
                    counter[i,j] = np.sum(matrix[i-1:i+2,j-1:j+2] * 1) - matrix[i,j]

    return counter
