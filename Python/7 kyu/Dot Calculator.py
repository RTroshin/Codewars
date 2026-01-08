def calculator(txt):
    x, symb, y = txt.split()
    x = len(x)
    y = len(y)

    if symb == '+':
        return '.' * (x + y)
    elif symb == '-':
        return '.' * (x - y)
    elif symb == '*':
        return '.' * (x * y)
    elif symb == '//':
        return '.' * int(x / y)
