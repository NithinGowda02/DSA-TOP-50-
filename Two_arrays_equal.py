def two_array(a, b):
    if len(a) != len(b):
        return False

    a.sort()
    b.sort()
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True
print(two_array([1,2,3,4],[1,2,3,5]))    