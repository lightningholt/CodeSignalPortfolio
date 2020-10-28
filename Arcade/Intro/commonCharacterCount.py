def commonCharacterCount(s1, s2):
    counter = 0
    used_chars = []
    
    for char1 in s1:
        for j in range(len(s2)):
            if char1 == s2[j]:
                if j not in used_chars:
                    counter += 1
                    used_chars.append(j)
                    break
    
    return counter
