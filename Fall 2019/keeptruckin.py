#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'goodSegment' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY badNumbers
#  2. INTEGER l
#  3. INTEGER r
#

def goodSegment(badNumbers, l, r):
    # Write your code here
    badNumbers = [num for num in badNumbers if num > l and num < r]

    badNumbers += [l]
    badNumbers += [r]

    badNumbers.sort()

    diff = []

    print(badNumbers)

    for i in range(1, len(badNumbers)):
        if i == len(badNumbers) - 1:
            diff += [badNumbers[i] - badNumbers[i - 1]] 
        else:
            diff += [badNumbers[i] - badNumbers[i - 1] - 1 ] 

    
    return max(diff)


if __name__ == '__main__':



#!/bin/python3

import sys
import os



# Complete the function below.

def jobOffers(scores, lowerLimits, upperLimits):
    result = []

    minScore = min(scores)
    maxScore = max(scores)

    

    for i in range(len(lowerLimits)):
        if minScore >= lowerLimits[i] and maxScore <= upperLimits[i]:
            result += [len(scores)]
        else:
            temp = 0
            for score in scores:
                if score >= lowerLimits[i] and score <= upperLimits[i]:
                    temp += 1
            
            result += [temp]

    return result

    # To solve this optimally, you would want to first sort the scores,
    # then binary search the scores based on lowerLimits and upperLimits.
    # After that, get the number of elements between those indices.
    # https://www.geeksforgeeks.org/queries-counts-array-elements-values-given-range/



if __name__ == "__main__":