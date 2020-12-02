import numpy as np 

def absoluteValuesSumMinimization(a):
    
    ab_diff_sum = 1e10
    tmp = 0
    ans = 0
    a = numpy.array(a)
    
    for i in range(len(a)):
        tmp = sum(abs(a[i]-a))
        
        if tmp < ab_diff_sum:
            ab_diff_sum = tmp
            ans = a[i]
            
    return ans
        


