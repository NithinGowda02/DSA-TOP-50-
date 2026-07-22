def longest_word(sentence):
    sentence = sentence.split()
    max_len = 0
    word_dict = {}
    for word in sentence:
        if len(word) > max_len:
            max_len = len(word)
            max_word = word
    word_dict[max_word] = max_len  
    return word_dict
print(longest_word("Hey hi good morning my name is Nithin"))      