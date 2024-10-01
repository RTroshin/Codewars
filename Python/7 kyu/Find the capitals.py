def capitals(word):
    res = []

    for ch in word:
        if ch.isupper():
            res.append(word.index(ch))

    return res
