def triple_x(str):
    if not str:
        return False

    for i, ch in enumerate(str):
        if ch == 'x' and str[i + 1] == 'x' and str[i + 2] == 'x':
            return True
        elif ch == 'x' and str[i + 1] != 'x':
            return False

    return False
