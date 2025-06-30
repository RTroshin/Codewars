def case_sensitive(s):
    resBool = True
    res = []

    for c in s:
        if c.isupper():
            resBool = False
            res.append(c)

    return [resBool, res]
