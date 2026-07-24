def frequency_char(s):
    freq = {}
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq
print(frequency_char("hello world"))            