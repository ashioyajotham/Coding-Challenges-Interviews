
def solution(parentheses):
    # Type your solution here 
    count_open = 0
    count_close = 0
    
    stack = []
#     for p in parentheses:
#         if p == '(':
#             count_open += 1
#         else:
#             count_close += 1
        
#     open = '(' * count_close
#     end = ')' * count_open
    
#     return open + parentheses + end

    for p in parentheses:
        if p == ")" and count_open:
            count_open -= 1
        elif p == "(":
            count_open += 1
        else:
            count_close += 1
    
    open = "(" * count_close
    end = ")" * count_open
    return open + parentheses + end
       
    
    
    
        
