def arithmeticExpression(a, b, c):
    '''
    Check if a # b == c for # in [+, -, *, /]
    '''
    if a/b == c:
        return True
    elif a - b == c:
        return True
    elif a * b == c:
        return True
    elif a + b == c:
        return True
    else:
        return False
