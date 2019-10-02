#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'areAlmostEquivalent' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY s
#  2. STRING_ARRAY t
#

def areAlmostEquivalent(s, t):
    # Write your code here
    result = []
    for i in range(len(s)):
        result += [checkEq(s[i], t[i])]


    return result


def checkEq(s, t):
    if len(s) != len(t):
        return "NO"
    

    else:
        sDict = {}
        tDict = {}
        
        for l in s:
            if l not in sDict:
                sDict[l] = 1
            else:
                sDict[l] += 1
            
        for l in t:
            if l not in tDict:
                tDict[l] = 1
            else:
                tDict[l] += 1
        

        for key in sDict.keys():
            
            if (key not in tDict and sDict[key] > 3) or (key in tDict and abs(sDict[key] - tDict[key]) > 3):
                return "NO"
        return "YES"

if __name__ == '__main__':





#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isPossible' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#  4. INTEGER d
#
sys.setrecursionlimit(5000)
def isPossible(a, b, c, d):
    # Write your code here
    if a == c and b == d:
        return "Yes"
    elif a > c or b > d:
        return "No"
    else:
        first = isPossible(a + b, b, c, d)
        second = isPossible(a, a + b, c, d)

        if first == "Yes" or second == "Yes":
            return "Yes"
       
    return "No"

# Recursion Depth Exceeded? Should find an iterative solution instead. :(

if __name__ == '__main__':