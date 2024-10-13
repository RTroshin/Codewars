def remove_chars(str):
    res = ''

    for ch in str:
        if ch.isalpha() or ch.isspace():
            res += ch

    return res
