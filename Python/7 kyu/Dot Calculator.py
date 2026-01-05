def calculator(txt):
    str = txt.split()
    x = str[0]
    y = str[2]
    symb = (str[1])

    if symb == '+':
        return str[0] + str[2]
    elif symb == '-':
        return str[0][len(str[2]):]
    elif symb == '*':
        return str[0] * len(str[2])
    elif symb == '//':
        return str[0][:len(str[0]) // len(str[2])]
