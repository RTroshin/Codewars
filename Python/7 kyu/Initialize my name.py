def initialize_names(name):
    res = ''
    name = name.split()

    if len(name) == 1:
        return name[0]
    elif len(name) == 2:
        return f"{name[0]} {name[1]}"

    for i in range(1, len(name) - 1):
        res += f"{name[i][0]}. "

    return f"{name[0]} {res}{name[-1]}"
