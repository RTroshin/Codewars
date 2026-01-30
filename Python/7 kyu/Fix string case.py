def solve(str):
    lower = 0
    upper = 0

    for ch in str:
        if ch.islower():
            lower += 1
        else:
            upper += 1

    if lower > upper:
        str = str.lower()
    elif lower < upper:
        str = str.upper()
    else:
        str = str.lower()

    return str
