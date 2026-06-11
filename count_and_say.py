def count_and_say(n):
    result = "1"
    for _ in range(n - 1):
        next_res = ""
        i = 0
        while i < len(result):
            count = 1
            while i + count < len(result) and result[i+count] == result[i]:
                count += 1
            next_res += str(count) + result[i]
            i += count
        result = next_res
    return result

print(count_and_say(4))