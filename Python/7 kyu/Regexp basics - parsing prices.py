def to_cents(amount):
    if not amount:
        return None
    elif amount[0] != '$' or '.' not in amount:
        return None

    res = amount[1:].split('.')

    return int(res[0] + res[1])
