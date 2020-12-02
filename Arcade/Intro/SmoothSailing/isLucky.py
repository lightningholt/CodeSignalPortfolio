def isLucky(n):
    '''
    n represents a lotto ticket number.
    Tickets are lucky if the sum of the first half of its digits equals the sum of the second half.
    For instance:
    n = '1230' is lucky.
    (1 + 2 = 3 + 0)
    but
    n = '239017' is not.
    (2 + 3 + 9 != 0 + 1 + 7)
    '''
    list_of_ints = [int(i) for i in str(n)]
    ll = len(str(n))
    if (ll % 2) != 0:
        return False
    else:
        list_of_ints = [int(i) for i in str(n)]

        half_len = ll//2
        first_half = sum(list_of_ints[:half_len])
        second_half = sum(list_of_ints[half_len:])

        if first_half == second_half:
            return True
        else:
            return False
