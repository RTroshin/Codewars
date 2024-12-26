def min_value(digits):
    digits = set(digits)

    digits = sorted(digits)

    digits = map(str, digits)

    digits = ''.join(digits)

    return int(digits)
