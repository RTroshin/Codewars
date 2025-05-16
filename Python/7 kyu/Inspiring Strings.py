def longest_word(string_of_words):
    string_of_words = string_of_words.split()[::-1]
    string_of_words_len = []

    for word in string_of_words:
        string_of_words_len.append(len(word))

    return string_of_words[string_of_words_len.index(max(string_of_words_len))]
