def capitalize(s, ind):
    res = ''

    for i in range(len(s)):
        if i in ind:
            res += s[i].upper()
        else:
            res += s[i]

    return res
