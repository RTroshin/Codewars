def to_cents(amount):
    if not amount:
        return None
    if amount[0] != '$':
        return None
    if '.' not in amount:
        return None

    res = amount[1:].split('.')
    res = res[0] + res[1]
    res = int(res)

    return res
