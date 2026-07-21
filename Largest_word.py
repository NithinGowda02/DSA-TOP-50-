def largest_word(s):
    s = s.split()
    large = s[0]
    for word in s:
        if len(word) > len(large):
            large = word
    return large
print(largest_word("I play cricket in my free time."))        