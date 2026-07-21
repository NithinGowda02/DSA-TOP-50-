def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

result = linear_search([1,2,3,4,5,6], 5)
if result != -1:
    print("Element found in index :", result)
else:
    print("Element not Found!")        