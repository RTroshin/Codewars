def adjacent_double_double_letters(word):
    for i in range(len(word)):
        if i < len(word) - 3 and word[i] == word[i + 1]:
            if word[i + 2] == word[i + 3]:
                return True

    return False
