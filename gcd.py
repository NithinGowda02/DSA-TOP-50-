def gcd(a, b):
    small = min(a,b)
    for i in range(small,0,-1):
        if a % i == 0 and b % i == 0:
            print("GCD/HCF : ",i)
            break  
print(gcd(18, 24))          