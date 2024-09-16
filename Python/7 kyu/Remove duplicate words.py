def remove_duplicate_words(s):
    res = []

    for w in s.split():
        if w not in res:
            res.append(w)

    return ' '.join(res)
