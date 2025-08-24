def remove(str):
    res = ''
    str = str[::-1]

    for ch in str:
        if ch == '!':
            res += ''
        else:
            res += ch

    return res[::-1]
