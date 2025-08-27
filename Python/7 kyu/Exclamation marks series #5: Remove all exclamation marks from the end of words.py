def remove(str):
    res = ''

    for ch in str[::-1]:
        if ch == '!':
            res += ''
        else:
            res += ch

    return res[::-1]
