# Complete the roverMove function below.
def roverMove(matrixSize, cmds):
    x, y = 0, 0
    
    for cmd in cmds: 
        if cmd == "LEFT":
            if y - 1 >= 0:
                y = y - 1
        elif cmd == "RIGHT":
            if y + 1 < matrixSize:
                y = y + 1
        elif cmd == "UP":
            if x - 1 >= 0:
                x = x - 1    
        else:
            if x + 1 < matrixSize:
                x = x + 1
                
            
    return matrixSize * x + y


# Complete the maxInversions function below.
def maxInversions(prices):
    count = 0
    
    for i in range(len(prices)):
        numLessThan = 0
        numGreaterThan = 0
        
        for j in range(i+1, len(prices)):
            if prices[j] < prices[i]:
                numLessThan += 1
        
        for j in range (0, i):
            if prices[j] > prices[i]:
                numGreaterThan += 1
        
        count += numGreaterThan * numLessThan
        
    return count
            