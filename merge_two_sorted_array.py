def merge_sort(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j+=1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

print(merge_sort([1,7,9,10,12],[2,4,6]))            