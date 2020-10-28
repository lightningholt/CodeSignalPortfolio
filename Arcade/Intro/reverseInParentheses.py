def reverseInParentheses(inputString):
    
    stack = [[]] # accumulate letters in stack[0]
    for l in inputString:
        if l == '(':
            stack.append([])        # start a new level
        elif l == ')':
            sub = stack.pop()[::-1] # pop the last level and reverse
            stack[-1].extend(sub)   # add to current 
        else:
            stack[-1].append(l)     # add to current

    x =''.join(stack[0]) # join everything back together
    
    return x
    
