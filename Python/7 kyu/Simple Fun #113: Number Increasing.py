def number_increasing(n: int) -> bool:
    i = 1

    if n == i:
        return True
    elif n == 3:
        return True
    elif n == 6:
        return True

    while i <= n:
        i *= 3

    if i == n:
        return True

    i = 1

    while i <= n:
        i += 5

    if i == n:
        return True

    return False
