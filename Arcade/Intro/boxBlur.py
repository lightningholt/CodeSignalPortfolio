import numpy as np

def boxBlur(image):
    '''
    I cheated and imported numpy for this one. But apply the box blur to an image
    '''

    x = len(image)
    y = len(image[0])

    new_pic = np.zeros((x-2,y-2))

    for i in range(1, x-1):
        for j in range(1, y-1):

            new_pic[i-1][j-1] = (sum(image[i-1][(j-1):(j+2)]) + sum(image[i][(j-1):(j+2)]) + sum(image[i+1][(j-1):(j+2)]))//9

    return new_pic
