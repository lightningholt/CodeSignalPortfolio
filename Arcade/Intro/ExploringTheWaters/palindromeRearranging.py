def palindromeRearranging(inputString):
    '''
    Given a string, find out if its characters can be rearranged to a palindrome
    For instance, 'aabb' can be rearranged to 'abba', which is a palindrome

    Solution:
    For a palindrome, each character except the middle one needs to appear twice.
    So count the number of instances of each character. If more than one character
    has an odd number of instances, then inputString cannot be made into a palindrome.
    '''
    counted_chars = []
    pal_counts = []

    for i in range(len(inputString)):

        if inputString[i] not in counted_chars:
            counted_chars.append(inputString[i]) #find list of unique chars
            # find instances of unique characters
            char_count = inputString.count(inputString[i])

            if char_count % 2 == 0:
                pal_counts.append(0)
            else:
                pal_counts.append(1)

    if sum(pal_counts) <= 1:
        return True
    else:
        return False
