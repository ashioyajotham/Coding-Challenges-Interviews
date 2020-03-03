#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'frequencyOfMaxValue' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY price
#  2. INTEGER_ARRAY query
#
# Find number of max value occurences of subarrays defined by
# element in array which specifies the k-th item as the start
# of the subarray of price. 

def frequencyOfMaxValue(price, query):
    # Write your code here
    result = []
    for i in query:
        curr = price[i - 1:]
        currMax = max(curr)

        count = 0
        for i in curr:
            if i == currMax:
                count += 1

        result += [count]
    return result

    # naive solution

if __name__ == '__main__':