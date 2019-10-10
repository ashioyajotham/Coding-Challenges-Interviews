#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'rankIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY values
#  2. INTEGER rank
#

def rankIndex(values, rank):
    # Write your code here

    totalScore = []
    
    for value in values:
        totalScore += [sum(value)]

    totalScoreCopy = [0] * len(totalScore)

    
    for i in range(len(totalScore)):
        totalScoreCopy[i] = totalScore[i]

    totalScoreCopy.sort(reverse=True)

    target = totalScoreCopy[rank -1]

    return totalScore.index(target)

    

if __name__ == '__main__':


#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'strangeSort' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY mapping
#  2. STRING_ARRAY nums
#

def strangeSort(mapping, nums):
    # Write your code here
    nums.sort(key= lambda x: int(remove_leading(convert(x))))
    return nums

def convert(num):
    temp = ""
    for s in num:
        temp += str(mapping.index(int(s)))
      
    return temp

def remove_leading(x):
    if x == "":
        return 0
    if x[0] != '0':
        return x
    
    return remove_leading(x[1:])


if __name__ == '__main__':


