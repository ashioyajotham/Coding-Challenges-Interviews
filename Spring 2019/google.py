# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    maxHeight = float('-inf')
    count = 0
    for num in A:
        if num > maxHeight:
            count += 1
            maxHeight = num

    return count
    

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(stores, houses):
    #write your code in Python 3.6
    stores.sort()
    result = []
    for house in houses:
        storeNum = binarySearch(stores, 0, len(stores) - 1, house)
        result.append(storeNum)
    
    return result
        
        
def binarySearch(array, left, right, target):
    
    if right >= left:
        m = left + (right - left) // 2
        
        if array[m] == target:
            return array[m]
        
        elif array[m] > target:
            return binarySearch(array, 1, m - 1, target)
        else:
            return binarySearch(array, m + 1, right, target)
            
    else:
        left_diff, right_diff = None, None
        
        if left >= 0 and left < len(array):
            left_diff = abs(array[left] - target)
        if right >= 0 and right < len(array):
            right_diff = abs(array[right] - target)
        
        if left_diff and right_diff:
            if left_diff < right_diff:
                return array[left]
                
            elif left_diff > right_diff:
                return array[right]
        
        else:
            if left_diff:
                return array[left]
            else:
                return array[right]

            
            
        
        
 