def vowel_indices(word):
    res = []

    for i, ch in enumerate(word):
        if ch.lower() in "aeiouy":
            res.append(i + 1)

    return res
