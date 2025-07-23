def solve(str, k):
    str = list(str)
    alph = 'a'
    count = 0

    while count != k:
        for ch in str:
            if alph in str:
                if ch == alph:
                    str[str.index(ch)] = ''
                    count += 1
                    break
            elif ord(alph) < 122:
                alph = chr(ord(alph) + 1)
            else:
                return ''

    return ''.join(str)
