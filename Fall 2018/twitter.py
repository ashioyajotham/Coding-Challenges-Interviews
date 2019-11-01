#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'restock' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY itemCount
#  2. INTEGER target
#

def restock(itemCount, target):
    # Write your code here

    curr = 0

    index = 0

    while (curr < target and index < len(itemCount)):
        curr += itemCount[index]
        index += 1

    return abs(target - curr)

if __name__ == '__main__':


#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'finalInstances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER instances
#  2. INTEGER_ARRAY averageUtil
#

def finalInstances(instances, averageUtil):
    # Write your code here
    maxInstances = 2 * 10 ** 8
    action = False
    stopCount = 0

    for util in averageUtil:
        print(util)
        
        if (action):
            stopCount += 1
            if (stopCount == 10):
                action = False
            continue      

        if util > 60:
            if (instances * 2 < maxInstances):
                instances *= 2
                action = True
                stopCount = 0
        
        if util < 25:
            if (instances > 1):
                instances /= 2
                instances = math.ceil(instances)
                action = True
                stopCount = 0    
        print(instances)
    return instances        

if __name__ == '__main__':



#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'carParkingRoof' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY cars
#  2. INTEGER k
#

def carParkingRoof(cars, k):
    # Write your code here
    cars.sort()

    if (len(cars) == k):
        return abs(cars[0] - cars[-1]) + 1

    currentMin = float('inf')
    for i in range(len(cars) - k):
        currentMin = min(cars[i + k - 1] - cars[i] + 1, currentMin)

    return currentMin
if __name__ == '__main__':

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMinimumDifference' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY a
#  2. STRING_ARRAY b
#

def getMinimumDifference(a, b):
    # Write your code here
    result = []

    for first, second in zip(a, b):
        if (len(first) != len(second)):
            result += ['-1']
        else:
            diff = 0
            firstDict = {}
            secondDict = {}

            for i in first:
                if i in firstDict:
                    firstDict[i] += 1
                else:
                    firstDict[i] = 1

            for i in second:
                if i in secondDict:
                    secondDict[i] += 1
                else:
                    secondDict[i] = 1
            
            for i in firstDict.keys():
                if i not in secondDict:
                    diff += firstDict[i]
                elif (firstDict[i] > secondDict[i]):
                    diff += firstDict[i] - secondDict[i]

            result += [str(diff)]

    return result

if __name__ == '__main__':