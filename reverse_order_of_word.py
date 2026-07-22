def reverse_order(s):
    s = s.split()
    return " ".join(s[::-1])

print(reverse_order("hello world"))    