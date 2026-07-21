def duplicate_element(arr):
    duplicates = set()
    seen = set()
    for i in arr:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)
    return duplicates
print(duplicate_element([1,2,3,4,1,3,4,5,6,7]))            