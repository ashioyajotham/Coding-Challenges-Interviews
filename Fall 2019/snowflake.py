#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'strokesRequired' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY picture as parameter.
#
import sys

sys.setrecursionlimit(9000)

def strokesRequired(picture):
    # Write your code here
    return connectedComponents(picture, len(picture))

# import numpy as np 
  
maxRow = 5000
maxCol = 5000
  
visited = []

for i in range(maxCol):
    row = []
    for j in range(maxRow):
        row.append(0)
    visited.append(row)

# Function that return true if mat[row][col]  
# is valid and hasn't been visited  
def isSafe(M, row, col, c, n, l) : 
                                          
    # If row and column are valid and element  
    # is matched and hasn't been visited then  
    # the cell is safe  
    return ((row >= 0 and row < n) and 
            (col >= 0 and col < l) and 
            (M[row][col] == c and not 
             visited[row][col]));  
  
# Function for depth first search  
def DFS(M, row, col, c, n, l) :  
  
    # These arrays are used to get row  
    # and column numbers of 4 neighbours  
    # of a given cell  
    rowNbr = [ -1, 1, 0, 0 ];  
    colNbr = [ 0, 0, 1, -1 ];  
  
    # Mark this cell as visited  
    visited[row][col] = True;  
  
    # Recur for all connected neighbours  
    for k in range(4) : 
        if (isSafe(M, row + rowNbr[k],  
                   col + colNbr[k], c, n, l)) : 
  
            DFS(M, row + rowNbr[k],  
                col + colNbr[k], c, n, l);  
  
# Function to return the number of  
# connectewd components in the matrix  
def connectedComponents(M, n) : 
  
    connectedComp = 0;  
    l = len(M[0]);  
  
    for i in range(n) : 
        for j in range(l) : 
            if (not visited[i][j]) :  
                c = M[i][j];  
                DFS(M, i, j, c, n, l);  
                connectedComp += 1;  
          
    return connectedComp;  

# Source: https://www.geeksforgeeks.org/number-of-connected-components-in-a-2-d-matrix-of-strings/
# This is the idea to solve it but didn't have time to implement.


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

    minUse = 9999

    if len(cars) == k:
        return cars[-1] - cars[0] + 1
    
    k = k - 1

    for i in range(0, len(cars) - k):
        if (cars[i + k] - cars[i]) + 1 < minUse:
            minUse = (cars[i + k] - cars[i]) + 1

    return minUse

if __name__ == '__main__':