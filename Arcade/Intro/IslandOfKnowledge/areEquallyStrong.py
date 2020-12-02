def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    '''
    Two arms are equally strong if they can lift the same weight. Evaluate if
    you and your friends arms are equally strong given the max weight they can all
    lift.
    '''
    yourArms = [yourLeft, yourRight]

    if yourLeft == friendsLeft:
        if yourRight == friendsRight:
            return True
        else:
            return False
    elif yourLeft == friendsRight:
        if yourRight == friendsLeft:
            return True
        else:
            return False
    else:
        return False
