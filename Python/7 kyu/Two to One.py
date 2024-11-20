def longest(a1, a2):
    sumStr = list(a1) + list(a2)
    sumStr = set(sumStr)
    sumStr = sorted(sumStr)

    return ''.join(sumStr)
