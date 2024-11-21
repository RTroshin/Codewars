def longest(a1, a2):
    sumStr = set(list(a1) + list(a2))
    sumStr = sorted(sumStr)

    return ''.join(sumStr)
