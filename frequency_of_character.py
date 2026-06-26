def frequency(s):
    character_dict = {}
    for char in s:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict
print(frequency("programming"))            

           

