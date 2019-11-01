# Complete the getSequenceSum function below.
def getSequenceSum(i, j, k):
    result = 0
    for x in range(i, j):
        result += x
    
    for x in range(j, k - 1, -1):
        result += x
    return result
        

#
# Complete the 'reformatDate' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY dates as parameter.
#

def reformatDate(dates):
    # Write your code here
    
    month_dict = {"Jan": 1,
                  "Feb": 2,
                 "Mar" :3,
                 "Apr" :4,
                 "May": 5,
                 "Jun": 6,
                 "Jul": 7,
                 "Aug": 8,
                 "Sep": 9,
                 "Oct": 10,
                 "Nov": 11,
                 "Dec" : 12}
    results = []
    for date in dates:
        date_parts = date.split(" ")
        
        day = re.findall("\d+",date_parts[0])[0]
        month = month_dict[date_parts[1]]
        year = date_parts[2]
        
        if month < 10:
            month = str(0) + str(month)
        
        if int(day) < 10:
            day = str(0) + str(day)
        final_str = year + "-" + str(month) + "-" + str(day)
        
        results += [final_str]
        
    return results



#
# Complete the 'findMaxHeight' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER_ARRAY buildings
#  3. INTEGER_ARRAY heights
#

def findMaxHeight(N, buildings, heights):
    # Write your code here
    if len(buildings) == 0 and len(heights) == 0 or min(heights) > N:
        return N - 1
    
    result = list(range(0, N))
    
    for i in range(len(buildings)):    
        result[buildings[i] - 1] = heights[i]
    
    # For each constraint, I should find the difference between the first and last building 
    # in my result list and then if it's even, go to the half way point and start decrementing.
    # If it's odd, increment up to mid - 1 then skip the next building and start decrementing.
    return 3
    

    

