def password(str):
    if len(str) < 8:
        return False

    res_up, res_low, res_dig = False, False, False

    for ch in set(str):
        if ch.isupper():
            res_up = True
        elif ch.islower():
            res_low = True
        elif ch.isdigit():
            res_dig = True

    return res_up and res_low and res_dig
