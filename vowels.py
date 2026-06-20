def vowel(s):
    vowels = ['a','e','i','o','u']
    count = {}
    for i in s.lower():
        if i in vowels:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1    
    return count
print(vowel("helloe"))        

