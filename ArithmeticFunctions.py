import operator
import re
    
   
def parse_expression(expression):
    tokens = re.findall(r'\d+\.?\d*|[+*/()-]', expression)
    return tokens
        
def brackets(tokens):
    stack=[]
    for token in tokens:
        if token == ')':
            sub_expression = []
            while stack and stack[-1] != '(':
                sub_expression.append(stack.pop())
            stack.pop()
            stack.append(str(evaluate_expression(sub_expression[::-1])))
        else:
            stack.append(token)
    return stack
        
def multiplication_division(tokens):
    i = 0
    while i < len(tokens):
        if tokens[i] in ('*','/'):
            left = float(tokens[i-1])
            right = float(tokens[i+1])
            if tokens[i]=='*':
                result = left * right
            else: 
                result = left / right
            tokens = tokens[:i-1] + [str(result)] + tokens[i+2:]
        else:
            i += 1
    return tokens
        
def addition_subtraction(tokens):
    i = 0 
    while i < len(tokens):
        if tokens[i] in ('+','-'):
            left = float(tokens[i-1])
            right = float(tokens[i+1])
            if tokens[i]== '+':
                result = left + right
            else:
                result = left - right
            tokens = tokens[:i-1]+[str(result)]+tokens[i+2:]
        else:
            i+=1
    return tokens  
        
def evaluate_expression(expression):
    # Tokenize the expression
    if isinstance(expression, str):
        tokens = parse_expression(expression)
    else:
        tokens = expression
    
    # Handle brackets
    tokens = brackets(tokens)
    
    # Handle multiplication and division
    tokens = multiplication_division(tokens)
    
    # Handle addition and subtraction
    tokens = addition_subtraction(tokens)
    
    # The final result should be the only token left
    return float(tokens[0])      

