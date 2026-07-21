# def find_duplicates(nums):
#     seen = set()
#     duplicates = []
#     for num in nums:
#         if num in seen:
#             duplicates.append(num)
#         else:
#             seen.add(num)
#     return duplicates

# print(find_duplicates([1, 2, 3, 1, 2, 5, 4, 6, 5, 4, 3]))      

def duplicate(num):
    seen = set()
    duplicate_list = []
    for i in num:
        if i in seen:
            duplicate_list.append(i)
        else:
            seen.add(i)
    return duplicate_list
print(duplicate([1, 2, 3, 4, 2, 3, 7, 8, 4]))            