def title_case(s):
    s = s.split()
    result = []
    for word in s:
        result.append(word[0].upper() + word[1:].lower())
    return " ".join(result)

print(title_case("hello coding world"))    