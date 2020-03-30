def anagram(a, b):
    
    charDict = {}
    
    for char in a:
        if char in charDict:
            charDict[char] += 1
        else:
            charDict[char] = 1
            
    
    for char in b:
        if char in charDict and charDict[char] != 0:
            charDict[char] -= 1
        else:
            return False
        
    
    # for char in a:
    #     if charDict[char] != 0:
    #         return False
    
    return True
    