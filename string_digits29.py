def digits(s):
    is_digit = True
    for ch in s:
        if ch < '0' or ch > '9':
            is_digit = False
    if is_digit:
        return f"String contains only digits"
    else:
        return f"String not only contains digits"  
print(digits("-1234"))    
          