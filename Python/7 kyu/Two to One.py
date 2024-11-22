def longest(a1, a2):
    sumStr = sorted(set(list(a1) + list(a2)))

    return ''.join(sumStr)
