def remove_chars(str):
    res = ''

    for ch in str:
        if ch not in "0123456789.+,|()[]{}=@/~;^$'<>?-!*&:#%_" and ch != '"':
            res += ch

    return res
