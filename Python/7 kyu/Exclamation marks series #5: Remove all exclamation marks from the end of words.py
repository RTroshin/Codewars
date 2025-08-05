def remove(st):
    res = ''
    st = st[::-1]

    for i in range(len(st)):
        if st[i] == '!':
            res += ''
        else:
            res += st[i]

    res = res[::-1]

    return res
