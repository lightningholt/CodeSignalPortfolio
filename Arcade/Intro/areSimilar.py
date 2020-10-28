def areSimilar(a, b):
    
    if a == b:
        return True 
    else:
        bad_inds = []
        for i in range(len(a)):
            if a[i] != b[i]:
                bad_inds.append(i)
        
        if len(bad_inds) > 2:
            return False
        elif len(bad_inds) == 2:
            if a[bad_inds[0]] == b[bad_inds[1]] and a[bad_inds[1]] == b[bad_inds[0]]:
                return True
            else:
                return False
        else:
            return False
