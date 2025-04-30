def whitespace(string):
    res = True

    for i in range(len(string)):
        if not string[i].isspace():
            res = False

    return res
