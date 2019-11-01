Given an array containing positive and negative integers, return the sum of the subarray with the maximum sum.

 

# [ 1, -2, 3, 4, -5, 6 ] => 8
# [3, 4, -5, 6] (beginning and end of the subarray with maximum sum)

# Enter your code here. Read input from STDIN. Print output to STDOUT

# [ 1, -2, 3, 4, -5, 6 ]  <- Given array

def isNumber(str):
	result = False
	decimal = False

	for i in range(len(str)):
		if ord(str[i]) >= 48 and ord(str[i]) < 57:
			result = True
		elif str[i] == '.':
			if decimal:
				return False
			decimal = True
		elif str[i] == '-':
			if i != 0:
				return False
		else:
			return False

	return result


# [1, -2, 3] <- subarray -> 2

# [3, 4] -> 7

# [3, 4, -5, 6] => 8

def maximumProduct(lst):
    maxAll = -float('inf')
    currMax = 0
    currMin = 1
    
    for i in range(len(lst)):
        
        currMax *= lst[i]
        currMin = min(currMin * lst[i], 1)
        
        if (maxAll < currMax):
            maxAll = currMax
            
        
        if currMax < 0:
            currMax = 1
        
            
    return maxAll

def maximumSum(lst):
    
    maxAll = -float('inf')
    currMax = 0
    
    for i in range(len(lst)):
        
        currMax += lst[i]
        
        if (maxAll < currMax):
            maxAll = currMax
        
        if currMax < 0:
            currMax = 0
            
    return maxAll


print(maximumProduct([ -1, -2, -3, -4, -5, -6]))

print(maximumSum([ -1, -2, -3, -4, -5, -6 ]))
print(maximumSum([1, -2, 3]))
print(maximumSum([3, 4]))
print(maximumSum([3, 4, -5, 6]))