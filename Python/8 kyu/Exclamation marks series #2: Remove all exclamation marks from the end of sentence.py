def remove(str):
    while str and str[-1] == '!':
        str = str[:-1]

    return str
