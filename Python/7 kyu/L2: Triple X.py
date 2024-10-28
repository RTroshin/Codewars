def triple_x(str):
    for i, ch in enumerate(str):
        if ch == 'x':
            return True if str[i + 1] == str[i + 2] == 'x' else False

    return False
