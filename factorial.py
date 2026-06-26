def fact(n):
    if n == 0 or n == 1 or n == 2:
        return n
    else:
        fact1 = n * fact(n-1)
        return fact1
print(fact(6))    



