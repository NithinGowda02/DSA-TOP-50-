def prime(n):
    prime_num = []
    
    for num in range(2, n+1):
        is_prime = True
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_num.append(num)    
    return prime_num

print(prime(20))        
