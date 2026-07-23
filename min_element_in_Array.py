def min_element(arr):
    if not arr:
        return None

    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val
print(min_element([23,12,45,34,67,2,67]))        