from collections import Counter
def anagram(s, t):
    return Counter(s) == Counter(t)
#alternate Way
def anagram_v2(s, t):
    return sorted(s) == sorted(t)

print(anagram_v2("tab","rat"))
