def remove(str):
    res = ''
    str = str[::-1]

    for i in range(len(str)):
        if str[i] == '!':
            res += ''
        else:
            res += str[i]

    return res[::-1]
