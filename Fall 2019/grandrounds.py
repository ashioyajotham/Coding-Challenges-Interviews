class Limiter 
    
    def __init__(self, limit):
        self.limit = 3 # per second
    
    def is_allowed(self, client_id):
        pass
    
    
    
# 3 per second
rt = Limiter(3)

rt.is_allowed("interviewerName") # 2:00:00:00
rt.is_allowed("interviewerName") # 2:00:00:01
rt.is_allowed("interviewerName") # 2:00:00:02
rt.is_allowed("interviewerName") # 2:00:00:03  #invalid
rt.is_allowed("interviewerName") # 2:00:01:00  #valid


interviewerName -> [2:00:00:00, 2:00:00:01, 2:00:00:02]

# Question is writing a rate limiting API
# The interviewer wrote all of this lmao...
