def largest(arr):
    if not arr:
        return []

    large = arr[0]
    for num in arr:
        if num > large:
            large = num
    return large
print(largest([]))        