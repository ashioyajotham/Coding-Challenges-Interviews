class IntegerTracker:
    def __init__(self):
        # Default values if nothing is tracked
        self.mode = None 
        self.modeDict = {}
        self.modeCount = None
        self.maxNum = float('-inf') 
        self.minNum = float('inf') 
        self.mean = None
        self.count = 0
        
    def track(self, num):
        if num > self.maxNum:
            self.maxNum = num
        
        if num < self.minNum:
            self.minNum = num
            
           
        if self.mode == None:
            self.mode = num
            self.modeDict[num] = 1
            self.modeCount = 1
        else:
            if num in self.modeDict:
                self.modeDict[num] += 1
            else:
                self.modeDict[num] = 1
            
            if self.modeDict[num] > self.modeCount:
                self.mode = num
                self.modeCount = self.modeDict[num]
            
        
        if self.mean == None:
            self.mean = num
        else:
            self.mean = (self.mean * self.count + num) / (self.count + 1)
            
        self.count += 1  
        
    def get_max(self):
        return self.maxNum
        
    def get_min(self):
        return self.minNum
    
    def get_mean(self):
        return self.mean
        
    def get_mode(self):
        return self.mode
        

