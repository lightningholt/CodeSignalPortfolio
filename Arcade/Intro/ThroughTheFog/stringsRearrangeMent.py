from itertools import permutations

def stringsRearrangement(inputArray):
    x = list(permutations(sorted(inputArray)))
    truth_list = []
    sub_list = []
    
    for i in range(len(x)):
        for j in range(len(x[i])-1):
            sub_list.append(isOneCharDiff(x[i][j], x[i][j+1]))
        
        truth_list.append(all(sub_list))
        sub_list = []
    
    return any(truth_list)
        


def isOneCharDiff(s1:str, s2:str):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    
    return count == 1

