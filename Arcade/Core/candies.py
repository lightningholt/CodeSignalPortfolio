def candies(n, m):
    '''
    There are n children and m candies, find the number of candies that each
    child can eat provided every child gets the same number of candies.
    '''
    return (m//n) * n
