#
# Complete the 'usernamesSystem' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY u as parameter.
#

def usernamesSystem(u):
    # Write your code here
    
    usernames = {}
    result = []
    for i in u:
        if i not in usernames:
            usernames[i] = 1
        else:
            usernames[i] += 1
            
        if usernames[i] == 1:
            result += [i]
        else:
            result += [i + str(usernames[i] - 1)]
            
    return result
        
        
        
#
# Complete the 'getUnallottedUsers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY bids
#  2. INTEGER totalShares
#

def getUnallottedUsers(bids, totalShares):
    # Write your code here
    #print(bids)
    
    result = [i for i in range(1, len(bids) + 1)]
    temp = bids
    while (totalShares != 0):
        if bids == [] or totalShares < 1:
            return result
        
        highest_bid = max(bids, key=lambda x: x[2])
        
        highest_bidders = [bid for bid in bids if bid[2] == highest_bid[2]]
        highest_bidders.sort(key=lambda x: x[3])
    
        if len(highest_bidders) == 1:
            if totalShares >= highest_bidders[0][1]:
                totalShares -= highest_bidders[0][1]
                result.remove(highest_bidders[0][0])
                bids.remove(highest_bidders[0])
            else:
                return result
        else: 
            count = 0
            while (len(highest_bidders) != 0 and totalShares > 0):
                if (1 <= totalShares):
                    highest_bidders[count % len(highest_bidders)][1] -= 1
                    totalShares -= 1
                    
                    if highest_bidders[count % len(highest_bidders)][1] == 0:
                        result.remove(highest_bidders[count % len(highest_bidders)][0])
                        bids.remove(highest_bidders[count % len(highest_bidders)])
                        highest_bidders.remove(highest_bidders[count % len(highest_bidders)])
                        count = 0
                        continue
                    
                else:
                    return result
                
                count += 1
                
    return result
        
        
# I tested this on Python Tutor (https://goo.gl/Zj6pHT) and the last case works on there.
# I've spent a lot of time debugging for that last case and I can't figure out why it's not working.


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
    
    dict = {}
    for i in range(1, len(sprints)):
        
        start, end = min(sprints[i - 1], sprints[i]), max(sprints[i - 1], sprints[i])
        
        for j in range(start, end + 1):
            if j not in dict:
                dict[j] = 1
            else:
                dict[j] += 1
    
    maxSprint = max(dict.values())
    result = [[k, v] for k, v in dict.items() if v == maxSprint]
    result = min(result, key=lambda x: x[0])[0]
    
    return result
    
    


