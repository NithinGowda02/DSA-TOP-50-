def second_largest_element(arr):
    second_largest = largest = float("-inf")
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

print(second_largest_element([12, 10, 23, 43, 15, 30, 40]))            