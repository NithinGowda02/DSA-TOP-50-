# def second_largest_element(arr):
#     second_largest = largest = float("-inf")
#     for num in arr:
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif num > second_largest and num != largest:
#             second_largest = num
#     return second_largest

# print(second_largest_element([12, 10, 23, 43, 15, 30, 40]))

def second_largest(num):
    largest_num = second_largest = float("-inf")
    for arr in num:
        if arr > largest_num:
            second_largest = largest_num
            largest_num = arr
        elif arr > second_largest and arr != largest_num:
            second_largest = arr
    return second_largest

print(second_largest([12, 124, 124, 26, 67, 89]))            