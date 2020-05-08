#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'compressedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING message as parameter.
#

def compressedString(message):
    # Write your code here

    result = message[0]
    count = 1

    for i in range(1, len(message)):
        if message[i] == message[i - 1]:
            count += 1
        else:
            if count > 1:
                result += str(count)
                count = 1                
            result += message[i]
        
    if count > 1:
        result += str(count)

    return result

if __name__ == '__main__':