# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    count = 1
    nextIndex = 0
    
    while (A[nextIndex] != -1):
        count += 1
        nextIndex = A[nextIndex]
        
    return count
        
        

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(ranks):
    # write your code in Python 3.6
    
    rankSet = set(ranks)
    count = 0
    
    for i in ranks:
        if i + 1 in rankSet:
            count += 1
        
    return count


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    
    result = bin(A * B)
    return sum([1 for i in result if i == "1"])