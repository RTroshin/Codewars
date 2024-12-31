def initials(name):
    res = ''
    name = name.split()

    for n in name:
        res += n[0].upper() + '.'

    res = res[:-1]

    return res + name[-1][1:]
