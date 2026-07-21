def nonRepeating_char(s):
    s = s.lower()
    count = {}
    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    for ch in s:
        if count[ch] == 1:
            print(f"First non Reapeating Character is {ch}")
            break
    else:
        print("There is no non Repeating Character") 

print(nonRepeating_char("Nithin"))            
