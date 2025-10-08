def capitals_first(text):
    res1 = []
    res2 = []

    for word in text.split():
        if word[0].isupper():
            res1.append(word)
        elif word[0].islower():
            res2.append(word)

    return ' '.join(res1 + res2)
