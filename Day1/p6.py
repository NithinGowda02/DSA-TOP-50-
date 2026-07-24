def duplicate(nums):
    seen = set()
    duplicates = []
    for i in nums:
        if i in seen:
            duplicates.append(i)
        else:
            seen.add(i)
    return seen
print(duplicate([1,2,3,4,5,4,5,3,6,2]))           