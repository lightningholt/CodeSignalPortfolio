# helper function
def find_bad_pair(sequence):
    for i in range(len(sequence)-1):
        if sequence[i+1] - sequence[i] <= 0:
            #if bad pair, return index
            return i
    # if no bad pair found, return -1
    return -1



def almostIncreasingSequence(sequence):
    j = find_bad_pair(sequence)

    if j == -1:
        # no bad pair case
        ans = True
    if find_bad_pair(sequence[:j] + sequence[j+1:]) == -1:
        # check if removing the indexed element solves it
        ans = True
    elif find_bad_pair(sequence[0:j+1] + sequence[j+2:]) == -1:
        # check if removing the indexed + 1 element solves it
        ans = True
    else:
        # it can't be done
        ans = False

    return ans
