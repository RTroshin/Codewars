def solve(st, k):
    st = list(st)
    alph = 'a'
    count = 0
    i = 0

    while count != k:
        if alph in st and len(st) > 1:
            if st[i] == alph:
                st[i] = ''
                st = ''.join(st)
                st = list(st)
                count += 1
                i = 0
            i += 1
        elif ord(alph) < 122:
            alph = chr(ord(alph) + 1)
            i = 0
        else:
            return ''

    return ''.join(st)
