def remove(str):
    while str.endswith('!'):
        str = str[:-1]

    return str
