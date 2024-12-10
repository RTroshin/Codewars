def explode(s):
    res = ''

    for c in s:
        res += c * int(c)

    return res
