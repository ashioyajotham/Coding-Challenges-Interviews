#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'ada' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER year as parameter.
#
import calendar
def ada(year):
    # Write your code here

    cal = calendar.Calendar() 
    count = 0
    for day, weekday in cal.itermonthdays2(year, 10):
        
        if weekday == 1 and day != 0:
            count += 1
        
        if count == 2:
            return day




if __name__ == '__main__':


#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the alert function below.
def alert(inputs, windowSize, allowedIncrease):
    minAvg = float('inf')
    allAvg = []

    for i in range(len(inputs)):
        average = 0
        for j in range(i, i + windowSize):
            if j >= len(inputs):
                break
            
            average += inputs[j]

        allAvg.append(average / windowSize)

        if average < minAvg:
            minAvg = average
        if (allowedIncrease * minAvg < average):
            return True
        
    for i in range(len(inputs)):
        count = 0
        for j in range(i - windowSize + 1, i + 1):
            if j < 0 or j >= len(allAvg):
                continue
            
            
            if (inputs[i] > allowedIncrease * allAvg[j]):
                count += 1
        
        if count == windowSize:
            return True

    return False


if __name__ == '__main__':