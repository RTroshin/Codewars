def remove_chars(s):
    res = ''

    for c in s:
        if c not in "0123456789.+,|()[]{}=@/~;^$'<>?-!*&:#%_" and c != '"':
            res += c

    return res
