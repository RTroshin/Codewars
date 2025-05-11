def to_cents(amount):
    if not amount or amount[0] != '$' or '.' not in amount:
        return None

    res = amount[1:].split('.')

    return int(res[0] + res[1]) if len(res[1]) == 2 else None
