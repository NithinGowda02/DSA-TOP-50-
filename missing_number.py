def missing_number(nums, n):
    expected_output = (n * (n + 1)) // 2
    sum_arr = sum(nums)
    return expected_output - sum_arr
print(missing_number([2,3,4,5,6] ,6))

      
