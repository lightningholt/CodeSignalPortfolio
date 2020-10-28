def tennisSet(score1, score2):
    '''
    Is score1:score2 a valid tennis set score? 
    '''

    high = max(score1, score2)
    low = min(score1, score2)

    if score1 == score2:
        return False
    elif high == 7:
        if low < 5:
            return False
        else:
            return True
    elif high == 6:
        if low == 5:
            return False
        else:
            return True

    else:
        return False
