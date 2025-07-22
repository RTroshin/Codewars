def solve(st, k):
    st = list(st)
    alph = 'a'
    count = 0

    while count != k:
        for ch in st:
            if alph in st:
                if ch == alph:
                    st[st.index(ch)] = ''
                    count += 1
                    break
            elif ord(alph) < 122:
                alph = chr(ord(alph) + 1)
            else:
                return ''

    return ''.join(st)
