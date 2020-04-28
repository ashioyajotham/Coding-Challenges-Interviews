#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'toolchanger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY tools
#  2. INTEGER k
#  3. STRING q
#

def toolchanger(tools, k, q):
    # Write your code here
    if tools[k] == q:
        return 0

    left = k - 1
    right = k + 1
    count = 1

    while True:
        if tools[left] == q or tools[right] == q:
            break

        left = (left - 1) % len(tools)
        right = (right + 1) % len(tools)
            
        count += 1
    return count

if __name__ == '__main__':


#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'cacheContents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY callLogs as parameter.
#

def cacheContents(callLogs):
    # Write your code here

    timeDict = {}
    cache = []
    minTime = float('inf') 
    maxTime = -float('inf')
    countDict = {}

    for time, item in callLogs:
        if time < minTime:
            minTime = time
        if time > maxTime:
            maxTime = time

        if time not in timeDict:
            timeDict[time] = [item]
        else:
            timeDict[time] += [item]

    
    for i in range(minTime, maxTime + 1):
        
        if i in timeDict:
            used = []
            for val in timeDict[i]:
                used += [val]
                if val in countDict:
                    countDict[val] += 2
                else:
                    countDict[val] = 2
    
            for key in countDict.keys():
                if key not in used:
                    countDict[key] = max(0, countDict[key] - 1)
        else: # no access in time i, decrement everyone
            for key in countDict.keys():
                countDict[key] = max(0, countDict[key] - 1)



    # 4/15 and the only visible case has 184 inputs -_-
    print(countDict)
    
    for key, value in countDict.items():
        if value > 5:
            cache += [key]   

    return cache

if __name__ == '__main__':


