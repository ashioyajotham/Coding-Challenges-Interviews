# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    neg = False
    
    if (N < 0):
        N = -N
        neg = True
    
    strN = str(N)
    result = []
    for i in range(len(strN)):
        temp = strN[:i] + '5' + strN[i:]
        
        result += [int(temp)]
        

    if neg:
        return -min(result)
    
    return max(result)
        
    
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math

def solution(A, B):
    # write your code in Python 3.6
    
    count = 0
    for i in range(A, B+1):
        if helper(i):
            count += 1
            
    return count


def helper(num):
    
    sqNum = int(math.sqrt(num))
    
    if (sqNum * (sqNum + 1) == num):
        return True
    
    return False
    
    