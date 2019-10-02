def evaluate2(expression):

    if expression == "":
        return 0

    if len(expression) == 1:
        return int(expression)
    
    if expression[0] == "+":
        return int(expression[2]) + evaluate2(expression[4:])
    
    elif expression[0] == "-":
        return int(expression[2]) - evaluate2(expression[4:])
        
    
evaluate2("+ 1 2")