def areSimilar(a, b):
    '''
    Find out if two arrays are similar, or if b_star ==a
    where b_star = b with two elements swapped
    For example:
    a = [1, 2, 3]
    b = [2, 1, 3]
    areSimilar(a,b) = True

    but
    a = [1, 2, 2]
    b = [2, 1, 1]
    areSimilar(a,b) = False

    '''
    if a == b:
        return True
    else:
        bad_inds = []
        # find indices of mismatched elements
        for i in range(len(a)):
            if a[i] != b[i]:
                bad_inds.append(i)

        if len(bad_inds) > 2:
            # too many mismatched elements
            return False
        elif len(bad_inds) == 2:
            # check if swapping mismatched elements works
            if a[bad_inds[0]] == b[bad_inds[1]] and a[bad_inds[1]] == b[bad_inds[0]]:
                return True
            else:
                return False
        else:
            return False
