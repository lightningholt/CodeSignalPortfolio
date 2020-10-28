def sortByHeight(a):
    
    sort_a = []
    pos_trees = []
    
    sort_heights = [None]*len(a)
    
    for i in range(len(a)):
        if a[i] == -1:
            pos_trees.append(i)
        else:
            sort_a.append(a[i])
    
    sort_a.sort()
    tree_count = 0
    for i in range(len(a)):
        if a[i] == -1:
            sort_heights[i] = -1
            tree_count += 1
        else:
            sort_heights[i] = sort_a[i-tree_count]
    
    return sort_heights
        


