def isLucky(n):
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
