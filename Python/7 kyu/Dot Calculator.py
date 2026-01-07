def calculator(txt):
    str = txt.split()
    x = len(str[0])
    y = len(str[2])
    symb = str[1]

    if symb == '+':
        return '.' * (x + y)
    elif symb == '-':
        return '.' * (x - y)
    elif symb == '*':
        return '.' * (x * y)
    elif symb == '//':
        return '.' * int(x / y)
