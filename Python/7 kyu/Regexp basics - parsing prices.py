def to_cents(amount):
    if not amount:
        return None
    elif amount[0] != '$':
        return None
    elif '.' not in amount:
        return None

    res = amount[1:].split('.')
    res = int(res[0] + res[1])

    return res
