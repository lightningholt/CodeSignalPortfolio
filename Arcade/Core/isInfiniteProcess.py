def isInfiniteProcess(a, b):
    '''
    Determine if a process will run infinitely. The process increases a by 1 and
    decreases b by 1 each step until a==b.
    '''
    if a> b:
        return True
    return (a-b) % 2 != 0
