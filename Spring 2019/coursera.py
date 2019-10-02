#
# Complete the 'mystery' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY letter as parameter.
#

def mystery(letter):
    # Write your code here
    result = []
    
    for word in letter:
        num_changes = 0
        if len(word) <= 1:
            result.append(0)
            continue
        
        m = len(word) // 2 
        if len(word) % 2 == 0: 
            start = m - 1
            end = m
        else:
            start = m - 1
            end = m + 1
        
        while (end < len(word)):
            left = ord(word[start])
            right = ord(word[end])
            num_changes += abs(left-right)
            start -= 1
            end += 1
        result.append(num_changes)

    return result
    
    
    
    
    