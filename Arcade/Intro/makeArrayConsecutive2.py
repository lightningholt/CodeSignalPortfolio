def makeArrayConsecutive2(statues):
    sort_statues = sorted(statues)
    nec_statues = 0
    n = len(statues)
    
    for i in range(n-1):
        if sort_statues[i+1] - sort_statues[i] > 1:
            nec_statues += sort_statues[i+1] - sort_statues[i] - 1
    return nec_statues
