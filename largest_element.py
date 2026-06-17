def largest_element(a):
    largest = a[0]
    for num in a:
        if num > largest:
            largest = num
    return largest

print(largest_element([12,4,7,8,15,23,4]))