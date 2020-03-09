# objective: Given a string containing an equation with parentheses, braces, and brackets, determine if the groupings are valid
# input: string
# output: boolean (true for valid groupings, false otherwise)
# examples:
# pass: '(5+3-{6/[2*1]})'
# fail: '(5+3-{6/[2*1)}]'

# def say_hello():
#     print('Hello, World')

# for i in range(5):
#     say_hello()

    
# (5+3-{6/[2*1]})

# (5+3-|6/[2*1]|)
# ||||
# |{|(||)}||
def checkBalance(s):
    
    seen = []
    
    
    left = ["(", "[","{"]
    right = [")", "]", "}"]
    
    pipe = -1
    
    for char in s:
        if char in left:
            seen.append(char) # seen = []
        
        elif char in right:
            if len(seen) == 0:
                return False
            
            if char == ")":
                if seen.pop() != "(":
                    return False
                
            elif char == "]":
                if seen.pop() != "[":
                    return False
                
            else:
                if seen.pop() != "{":
                    return False
        elif char == "|":
            if pipe == -1:
                pipe = 0
            
            else:
                if len(seen) != 0:
                    return False
                
                pipe = -1
                
    if len(seen) != 0 or pipe != -1:
        return False
    
    return True
                
        
print(checkBalance('(5+3-{6/[2*1]})'))
print(checkBalance('(5+3-{6/[2*1)}]'))

print(checkBalance('[((()))])))'))
print(checkBalance('[[[()]'))