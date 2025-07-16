def solve(st, k):
    st = list(st)
    alph = 'a'
    count = 0
    i = 0

    while count != k:
        if alph in st:
            if st[i] == alph:
                st[i] = ''
                count += 1
        elif ord(alph) < 122:
            alph = chr(ord(alph) + 1)
            i = 0
        else:
            return ''
        i += 1

    st = ''.join(st)

    return st
