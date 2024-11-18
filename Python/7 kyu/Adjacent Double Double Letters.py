def adjacent_double_double_letters(word):
    lenWord = len(word)

    for i in range(lenWord):
        if i < lenWord - 3 and word[i] == word[i + 1]:
            if word[i + 2] == word[i + 3]:
                return True

    return False
