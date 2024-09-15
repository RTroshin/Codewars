def remove_duplicate_words(s):
    res = []

    for w in s.split():
        if s.count(w) >= 1 and w not in res:
            res.append(w)

    return ' '.join(res)
