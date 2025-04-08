def initialize_names(name):
    res = ''
    name = name.split()

    if len(name) < 2:
        return ''.join(name)

    for i in range(1, len(name) - 1):
        res += f"{name[i][0]}. "

    return f"{name[0]} {res}{name[-1]}"
