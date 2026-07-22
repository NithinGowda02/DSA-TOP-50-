# def valid_parenthesis(s):
#     stack = []
#     mapping = {')':'(', ']':'[', '}':'{'}
#     for char in s:
#         if char in mapping:
#             top = stack.pop() if stack else '#'
#             if mapping[char] != top:
#                 return False
#         else:
#             stack.append(char) 

#     return not stack

# print(valid_parenthesis("(){}[]"))
# print(valid_parenthesis("({[]})"))           

def valid_parenthesis(s):
    stack = []
    mapping = {')':'(', ']':'[', '}':'{'}
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:    
            stack.append(char)
    return len(stack) == 0
print(valid_parenthesis("([))"))        
