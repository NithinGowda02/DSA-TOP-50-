def common_element(a, b):
    freq = {}
    result = []
    for i in a:
        freq[i] = 1

    for j in b:
        if j in freq and j not in result:
            result.append(j)
    return result
print(common_element([1,2,3,4],[2,3,4,5]))            