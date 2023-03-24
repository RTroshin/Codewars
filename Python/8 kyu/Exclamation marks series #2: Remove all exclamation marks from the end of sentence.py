def remove(str):
    for ch in str[::-1]:
        if ch is '!':
            str = str[:-1]
        else:
            break

    return str
