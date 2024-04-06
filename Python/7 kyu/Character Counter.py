def validate_word(word):
    word = word.lower()
    first_ch = word.count(word[0])

    return not [False for ch in word if word.count(ch) != first_ch]
