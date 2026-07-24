def second_largest(arr):
    large = sec_large = float("-inf")
    for num in arr:
        if num > large:
            sec_large = large
            large = num
        elif num > sec_large and num != large:
            sec_large = num
    return sec_large
print(second_largest([12, 34, 24, 56, 48]))            