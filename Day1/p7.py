def missing_number(arr):
    n = len(arr)+1
    exp_output = n*(n+1)//2
    result = sum(arr)
    final = exp_output - result
    return final
print(missing_number([1,2,4,5,6]))