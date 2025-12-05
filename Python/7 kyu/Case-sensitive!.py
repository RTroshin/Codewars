def case_sensitive(str):
    resBool = True
    res = []

    for ch in str:
        if ch.isupper():
            resBool = False
            res.append(ch)

    return [resBool, res]
