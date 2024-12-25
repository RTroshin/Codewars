def min_value(digits):
    digits = set(digits)

    digits = sorted(digits)

    digits = map(str, digits)

    digits = ''.join(digits)

    digits = int(digits)

    return digits
