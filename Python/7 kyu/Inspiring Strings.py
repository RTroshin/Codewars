def longest_word(string_of_words):
    string_of_words = string_of_words.split()[::-1]
    string_of_words_len = [len(word) for word in string_of_words]

    return string_of_words[string_of_words_len.index(max(string_of_words_len))]
