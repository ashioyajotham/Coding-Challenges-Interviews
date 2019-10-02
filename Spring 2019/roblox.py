#
# Complete the 'deleteOdd' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST_NODE.
# The function accepts INTEGER_SINGLY_LINKED_LIST_NODE listHead as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteOdd(listHead):
    # Write your code here
#     return_ptr = listHead

#     while (return_ptr is not None and return_ptr.data % 2 == 1):
#         return_ptr = return_ptr.next
    
#     listHead = return_ptr
    
#     prev = listHead
#     next = listHead
    # if listHead % 2 != 0 and listHead.next is not None:
    #     prev = listHead.next
    
    while (listHead is not None and listHead.data % 2 == 1):
        listHead = listHead.next
        
    return_ptr = listHead
    
    prev = listHead
    next = listHead.next
    while (prev is not None and prev.next is not None):
        if next.data % 2 == 1:
            next = next.next
            prev.next = next
        else:
            prev = next
            next = next.next
            
        
    return return_ptr
    # if listHead is None:
    #     return
    # if listHead.head % 2 == 0:
    #     return SinglyLinkedList()
    # else:
    #     return SinglyLinkedList(list.head, deleteOdd)





#
# Complete the 'palindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindrome(s):
    # Write your code here
    dict = {}
    for start in range(len(s)):
        for end in range(start, len(s)):
            sub = s[start:end+1]
            if sub == sub[::-1]:
                dict[sub] = 1

    return len(dict)
            
            
            
#
# Complete the 'minPower' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def minPower(p):
    # Write your code here

    result = [0] * len(p)
    
    running_sum = 0
    for i in range(len(p)):
        running_sum += p[i]
        result[i] = running_sum
    
    answer = min(result)
    
    if answer < 0:
        return -answer + 1
    else:
        return answer + 1