def min_value(digits):
    digits = sorted(set(digits))

    digits = ''.join(map(str, digits))

    return int(digits)
