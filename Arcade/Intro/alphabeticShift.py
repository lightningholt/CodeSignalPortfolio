def alphabeticShift(inputString):
    '''
    For each character in inputString replace with the next character (z -> a)
    '''
    new_str = ''
    new_char = 0

    for i in inputString:
        if i == 'z':
            new_char = ord('a')
        else:
            new_char = ord(i) + 1

        new_str += chr(new_char)

    return new_str
