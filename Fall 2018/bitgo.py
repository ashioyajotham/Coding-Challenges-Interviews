#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isPrime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def isPrime(n):
    # Write your code here

    if n > 1:
        for i in range(2, n):
            if (n % i == 0):
                return i
        
        else:
            return 1
    else:
        return 1
if __name__ == '__main__':





# you want at least 2 cooldown characters ('.') between duplicated tasks
# so schedule('aba', 2) outputs ab.a since b only counts as one cooldown


#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the schedule function below.
def schedule(tasks, cooldown):

    result = tasks[0]
    seen = dict()
    seen[tasks[0]] = 0
    for i in range(1, len(tasks)):


        if (tasks[i] in seen):
            #if (i - seen[tasks[i]]) <= cooldown:
            result += (cooldown - (i - seen[tasks[i]]) + 1) * '.' + tasks[i]
            seen.pop(tasks[i])
            # else:
            #     result += tasks[i]
            #     seen.pop(tasks[i])
        else:
            result += tasks[i]
            seen[tasks[i]] = i

    return result

if __name__ == '__main__':


#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def maxDifference(a):
    # Write your code here
    
    currMax = a[0]
    flag = False
    for i in range(1, len(a)):
        if (a[0] < a[i]):
            flag = True
    
    if (not flag):
        return -1


    minV = a[0]
    maxV = 0

    for i in range(len(a)):
        if (a[i] < minV):
            minV = a[i]
        elif (a[i] - minV > maxV):
            maxV = a[i] - minV

        
    return maxV


if __name__ == '__main__':