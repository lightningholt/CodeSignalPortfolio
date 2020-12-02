def checkPalindrome(inputString):
    #check if inputstring is the same forwards and backwardss
    if inputString == inputString[::-1]:
        return True
    else:
        return False
