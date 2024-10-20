def nothing_special(st):
    if type(st) is not str:
        return "Not a string!"

    res = ''

    for ch in st:
        if ch.isalpha() or ch.isdigit() or ch.isspace():
            res += ch

    return res
