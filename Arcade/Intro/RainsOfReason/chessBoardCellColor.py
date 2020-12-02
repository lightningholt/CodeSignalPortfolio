import numpy as np
from scipy import linalg

def chessBoardCellColor(cell1, cell2):
    '''
    Check if a bishop can move between cell1 and cell2 on a chess board.
    cells are given as A1 or similar (through H8)
    '''
    chessArray = np.array([True, False, True, False, True, False, True, False])
    chessArray = linalg.circulant(chessArray)

    ind_1 = []
    ind_2 = []
    
    for i in cell1:
        if i.isnumeric():
            ind_1.append(int(i)-1)
        else:
            ind_1.append(ord(i)- ord('A'))

    for i in cell2:
        if i.isnumeric():
            ind_2.append(int(i)-1)
        else:
            ind_2.append(ord(i)- ord('A'))

    check_color = chessArray[ind_1[0], ind_1[1]] ^ chessArray[ind_2[0], ind_2[1]]

    return not check_color
