def bubble_sort(num):
    n = len(num)
    for i in range(n):
        for j in range(0, n-i-1):
            if num[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
    return num
print(bubble_sort([1,5,2,4,3,6,7,9,8]))            
