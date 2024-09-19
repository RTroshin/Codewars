def remove_duplicate_words(str):
    res = str.split()[0]

    for wrd in str.split():
        if wrd not in res:
            res += ' ' + wrd

    return res
