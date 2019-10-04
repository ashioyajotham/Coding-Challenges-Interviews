#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bestPros' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY pros
#  2. INTEGER k
#

def bestPros(pros, k):
    # Write your code here

    scores = []
    maxDist = pros[0][0]
    for dist, rating in pros:
        maxDist = max(maxDist, dist)

    index = 0
    for dist, rating in pros:
        scores += [((maxDist - dist) * rating, index)]
        index += 1

    scores.sort(key=lambda x: x[0], reverse=True)
    scores = scores[:k]

    scores = [score[1] for score in scores]

    return scores
    
    
    


if __name__ == '__main__':


# gave up on this one... 4/16
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'categorySuggestions' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY categories
#  2. STRING_ARRAY projects
#  3. INTEGER k
#

def categorySuggestions(categories, projects, k):
    # Write your code here
    result = []
    lookup = dict()
    for category in categories:
        first, second, rel = category.split(",")
        
        if first not in lookup:
            lookup[first] = dict()

        lookup[first][second] = float(rel)

        if second not in lookup:
            lookup[second] = dict()
        
        lookup[second][first] = float(rel)
    
    for project in projects:
        lookup[project][project] = 1
    
        currRel = list(lookup[project].items())
        currRel.sort(key=lambda x: x[0])
        currRel.sort(key=lambda x: x[1], reverse=True)
        

        currRel = currRel[:k]
        currRel = [rel[0] for rel in currRel]

        result += [currRel]
    return result
    

if __name__ == '__main__':