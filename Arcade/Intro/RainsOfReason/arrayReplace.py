import numpy as np

def arrayReplace(inputArray, elemToReplace, substitutionElem):
    '''
    Replace elemToReplace in inputArray with substitionElem.
    '''
    inputArray = np.array(inputArray)

    inputArray[inputArray==elemToReplace] = substitutionElem

    return inputArray
