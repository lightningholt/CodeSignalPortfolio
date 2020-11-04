def baseConversion(n, x):
    '''
    Convert integer n to base 16.
    '''
    return hex(int(n,x))[2:]
