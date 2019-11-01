# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python
    if S == "":
        return -1
    
    string = " ".join(S.lower().split()).split(" ")
    
    for i in range(0, len(string), 2):
    
        if string[i] == "--count":
            try:
                if len(string) <= i + 1 or int(string[i + 1]) < 10 or int(string[i + 1]) > 100:
                    return -1
            except:
                return -1
                
        
        elif string[i] == "--name":
            if len(string) <= i + 1 or (i + 1 < len(string) and len(string[i + 1]) < 3 or len(string[i + 1]) > 10):
                return -1
            
            
        elif string[i] == "--help":
            if len(string) <= i + 1:
                return 1
            else:
                return -1
        else:
            return -1
        
    return 0
    
# Maybe I should parse this recursively...    
