def variableName(name):
    '''
    Check if a name is a valid variable name (starts with an English character
    only contains _ as special symbol)
    '''
    ans = True

    if name[0].isalpha() or name[0]=='_':
        for i in name[1:]:
            if i.isalpha():
                continue
            elif i.isnumeric():
                continue
            elif i == '_':
                continue
            else:
                ans = False
    else:
        ans = False

    return ans
