def isIPv4Address(inputString):
    '''
    for an input string determine if it matches IPv4 address format
    ###.###.###.### where ### > 0 and ### < 255 with no leading zeros.
    '''
    str_array = inputString.split('.')
    num_array = []
    for i in str_array:
        if i.isdigit():
            if int(i) <= 9:
                if len(i) > 1:
                    return False
                else:
                    num_array.append(int(i))
            else:
                num_array.append(int(i))

        else:
            return False


    if len(num_array) != 4:
        return False
    else:
        satisfy_array = []
        for j in num_array:
            if j >= 0 and j <= 255:
                satisfy_array.append(0)
            else:
                satisfy_array.append(1)

        if sum(satisfy_array) > 0:
            return False
        else:
            return True
