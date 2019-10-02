#
# Complete the 'getMostVisited' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY sprints
#

def getMostVisited(n, sprints):
    # Write your code here
    
    count = dict()
    for i in range(1, n + 1):
        count[i] = 0
        
    
    for i in range(len(sprints) - 1):
        start = min(sprints[i], sprints[i + 1])
        end = max(sprints[i], sprints[i + 1])
        
        for j in range(start, end + 1):
            count[j] += 1
            
        
    item = list(count.items())
    
    return max(item, key=lambda x: x[1])[0]


def get_top_of_hill(num_lots, get_altitude):
    """
    Parameters:
        num_lots (int): The number of lots.
        get_altitude (Callable[[int], int]): Function that takes a 0-based index
            of a lot, and returns its altitude. Raises a ValueError when given
            an invalid lot index.
    
    Returns:
        The 0-based index of any top of the hill lot.
    """
    lots = []
    for i in range(num_lots):
        lots += [get_altitude(i)]
    if (num_lots < 3):
        return lots.index(max(lots))
    
    else:
        for i in range(num_lots - 2):
            if (lots[i] < lots[i + 1] and lots[i + 1] > lots[i + 2]):
                return i + 1
    
    if (lots[-1] > lots[-2]):
        return num_lots - 1

    
    return -1