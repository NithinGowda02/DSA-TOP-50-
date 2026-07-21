def amstrong(num):  
    temp = num
    digits = len(str(num))
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** digits
        temp = temp // 10
    if sum == num:
        print("Its an Amstrong Number")
    else:
        print("Its not a Amstrong Number")

print(amstrong(1634))