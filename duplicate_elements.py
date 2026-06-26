def find_duplicates(nums):
    seen = set()
    duplicates = []
    for num in nums:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

print(find_duplicates([1, 2, 3, 1, 2, 5, 4, 6, 5, 4, 3]))      
