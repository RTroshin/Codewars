def initials(name):
    name = name.split()
    return '.'.join(n[0].upper() for n in name) + name[-1][1:]
