def maximum_char(s):
    if not s:
        return None

    max_char = s[0]
    max_count = 1

    current_char = s[0]
    current_count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            current_char = s[i]
            current_count += 1
        else:
            current_char = s[i]
            current_count = 1

        if current_count > max_count:
            max_char = current_char
            max_count = current_count 
    return max_char, max_count
print(maximum_char("aabbbbbcccc"))                   