def longest_word(string_of_words):
    string_of_words = string_of_words.split()
    max_word = string_of_words[0]

    for word in string_of_words:
        if len(max_word) < len(word):
            max_word = word

    return max_word
