def vowel_indices(word):
    res = []

    for i in range(len(word)):
        if word[i].lower() in "aeiouy":
            res.append(i + 1)

    return res
