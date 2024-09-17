def remove_duplicate_words(str):
    res = []

    for wrd in str.split():
        if wrd not in res:
            res.append(wrd)

    return ' '.join(res)
