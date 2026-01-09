def calculator(txt):
    x, symb, y = txt.split()

    if symb == '+':
        return '.' * (len(x) + len(y))
    elif symb == '-':
        return '.' * (len(x) - len(y))
    elif symb == '*':
        return '.' * (len(x) * len(y))
    elif symb == '//':
        return '.' * int(len(x) / len(y))
