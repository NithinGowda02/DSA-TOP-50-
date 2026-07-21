def count_occurances(ele, k):
    count = 0
    for el in ele:
        if k == el:
            count += 1
    return count
print(count_occurances([1,2,3,4,2,4,4,3,5,6,5,8], 4))    