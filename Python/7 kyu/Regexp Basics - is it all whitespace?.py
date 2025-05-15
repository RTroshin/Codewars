def whitespace(str):
    res = True

    for i in range(len(str)):
        if not str[i].isspace():
            res = False

    return res
