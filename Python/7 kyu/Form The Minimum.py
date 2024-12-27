def min_value(digits):
    digits = set(digits)

    digits = sorted(digits)

    digits = ''.join(map(str, digits))

    return int(digits)
