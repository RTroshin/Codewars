def longest(str1, str2):
    sumStr = sorted(set(list(str1) + list(str2)))

    return ''.join(sumStr)
