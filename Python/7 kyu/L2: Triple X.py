def triple_x(str):
    if not str:
        return False

    for i in range(len(str)):
        if str[i] == 'x' and str[i + 1] == 'x' and str[i + 2] == 'x':
            return True
        elif str[i] == 'x' and str[i + 1] != 'x':
            return False

    return False
