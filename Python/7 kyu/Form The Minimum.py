def min_value(digits):
    digits = ''.join(map(str, sorted(set(digits))))

    return int(digits)
