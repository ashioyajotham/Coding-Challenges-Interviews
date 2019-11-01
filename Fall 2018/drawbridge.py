#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countStudents' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY height as parameter.
#

def countStudents(height):
    # Write your code here

    copy = [h for h in height]
    copy.sort()

    result = 0
    for i in range(len(height)):
        if height[i] != copy[i]:
            result += 1
    
    return result

if __name__ == '__main__':




#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMostVisited' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY sprints
#

def getMostVisited(n, sprints):
    # Write your code here

    dict = {}


    # start = min(sprints)
    # end = max(sprints)

    for i in range(len(sprints) - 1):
        
        start, end = min(sprints[i], sprints[i + 1]), max(sprints[i], sprints[i + 1])
        for j in range(start, end + 1):
            if j not in dict:
                dict[j] = 1
            else:
                dict[j] += 1
    
    print(dict)

    result = list(dict.keys())
    result.sort()
    return max(result, key=lambda x: dict[x])


# Maybe I can keep track of a range and update
# where is the most overlapped based on whether 
# the next position is greater or less


if __name__ == '__main__':