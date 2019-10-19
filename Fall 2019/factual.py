# readings: list of [timestamp, speed] tuples.
#   timestamp is in seconds
#   speed is in km/h
# end_time: time at which truck speed is requested, in seconds

def solution(readings, end_time):
    # Type your solution here 
    
    total = 0
    for i in range(1, len(readings)):
        distTraveled = readings[i][0] - readings[i - 1][0]
        total += readings[i - 1][1] / 3600 * distTraveled
        
    total += readings[-1][1] / 3600 * (end_time - readings[-1][0])
    return total
        
        


def solution(clients):
    # Type your solution here 
    
    clientXs = [client[0] for client in clients]
    clientYs = [client[1] for client in clients]
    
    midX = (min(clientXs) + max(clientXs)) // 2
    midY = (min(clientYs) + max(clientYs)) // 2
    
    diff = 0
    
    for i in range(len(clients)):
        
        diff += abs(clientXs[i] - midX)
        diff += abs(clientYs[i] - midY)
        
    return diff
    
        
def solution(modulesToBuild, dependencies):
    
    total = set(modulesToBuild)
    
    for x, y in dependencies:
        total.add(x)
        total.add(y)
        
    return len(total)
    