def initials(name):
    name = name.split()

    res = ''.join(n[0].upper() + '.' for n in name)

    return res[:-1] + name[-1][1:]
