def switcheroo(str):
    str = list(str)

    for i in range(len(str)):
        if str[i] == 'a':
            str[i] = 'b'
        elif str[i] == 'b':
            str[i] = 'a'

    return ''.join(str)
