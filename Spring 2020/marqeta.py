#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'firstRepeatedWord' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

import re

def firstRepeatedWord(sentence):
    # Write your code here

    words = re.findall('\w+', sentence)

    seen = dict()

    for word in words:
        if word in seen:
            return word
        else:
            seen[word] = 1

    return None
if __name__ == '__main__':


#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'subarraySum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def subarraySum(arr):
    # Write your code here
    result = 0

    for i in range(len(arr)):
        
        result += arr[i] * (i + 1) * (len(arr) - i)

    return result
if __name__ == '__main__':