def initials(name):
    res = ''
    name = name.split()

    for n in name:
        res += n[0].upper() + '.'

    return res[:-1] + name[-1][1:]
