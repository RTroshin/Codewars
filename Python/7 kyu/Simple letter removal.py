def solve(st, k):
    st = list(st)
    alph = 'a'
    count = 0

    while count != k:
        for i in range(len(st)):
            if alph in st:
                if st[i] == alph:
                    st[i] = ''
                    count += 1
                    break
            elif ord(alph) < 122:
                alph = chr(ord(alph) + 1)
            else:
                return ''

    return ''.join(st)
