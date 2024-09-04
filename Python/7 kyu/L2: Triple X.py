def triple_x(str):
    for i, ch in enumerate(str):
        if ch == 'x' and str[i + 1] == str[i + 2] == 'x':
            return True
        elif ch == 'x' and str[i + 1] != 'x':
            return False

    return False
