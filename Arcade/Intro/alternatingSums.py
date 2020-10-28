def alternatingSums(a):
    w1 = 0
    w2 = 0
    for i in range(len(a)):
        if i%2 == 0:
            w1 += a[i]
        else:
            w2 += a[i]
    
    return [w1, w2]
