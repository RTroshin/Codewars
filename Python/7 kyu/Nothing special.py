def nothing_special(st):
    if not isinstance(st, str):
        return "Not a string!"

    res = ''

    for ch in st:
        if ch.isalpha() or ch.isdigit() or ch.isspace():
            res += ch

    return res
