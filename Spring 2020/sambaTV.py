# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# Given string S of length N consisting only of letters A and/or B. 
# Find the minimum deletion to obtain a string in the format A...AB...B
# by deleting letters from S.

def solution(S):
    # write your code in Python 3.6
    
    leftB = []
    bSoFar = 0
    for i in range(len(S)):
        leftB += [bSoFar]
        
        if S[i] == 'B':
            bSoFar += 1
            
    
    rightA = [0] * len(S)
    aSoFar = 0
    for j in range(len(S)-1, -1, -1):
        rightA[j] = aSoFar
        
        if S[j] == 'A':
            aSoFar += 1
    
    minDelete = len(S)
    
    for i in range(len(S)):
        if (rightA[i] + leftB[i] < minDelete):
            minDelete = rightA[i] + leftB[i]
            
    return minDelete
    