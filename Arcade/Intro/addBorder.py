def addBorder(picture):
    #given a rectangular array of characters, add a border of asterisks to it
    # Ex. picture =  ['abc', 'ded']
    # addBorder(picture) = ['*****', '*abc*','*ded*', '*****']
    
    array_lengths = [len(i) for i in picture]
    longest_pic = max(array_lengths)
    new_length = longest_pic+2
    border_pic = ["*"*new_length]
    
    for j in range(len(picture)):
        needed_stars = len(picture[j]) - longest_pic + 1
        star_pic = '*'*needed_stars+picture[j]+'*'*needed_stars
        border_pic.append(star_pic)
    
    border_pic.append("*"*new_length)
    
    return border_pic
