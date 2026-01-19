def case_sensitive(str):
    res = []

    for ch in str:
        if ch.isupper():
            res.append(ch)

    return [False, res] if res else [True, []]
