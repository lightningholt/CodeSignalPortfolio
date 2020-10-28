def reachNextLevel(experience, threshold, reward):
    '''
    Given your experience and the reward, did you level up (aka surpass threshold)?
    '''
    return experience + reward >= threshold
