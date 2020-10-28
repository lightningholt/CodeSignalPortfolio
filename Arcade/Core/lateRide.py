def lateRide(n):
    '''
    Find the sum of the time displayed at hh:mm given that you left at 00:00
    and rode for n minutes.
    '''
    return sum([int(char) for char in str(n//60)+str(n%60)])
