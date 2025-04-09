def initialize_names(name):
    name = name.split()

    if len(name) < 3:
        return ' '.join(name)

    return f"{name[0]} {'. '.join([name[i][0] for i in range(1, len(name) - 1)])}. {name[-1]}"
