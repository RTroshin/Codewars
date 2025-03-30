def longest_word(string_of_words):
    string_of_words = string_of_words.split()
    max_word = string_of_words[0]

    for i in range(len(string_of_words)):
        if len(max_word) < len(string_of_words[i]):
            max_word = string_of_words[i]

    return max_word
