def listBeautifier(a):
    '''
    A list is beautiful when the first and last element are the same.
    Remove the first and last elements from list, until the list is beautiful.
    '''
    res = a[:]
    while res and res[0] != res[-1]:
        _, *res, _ = res
    return res
