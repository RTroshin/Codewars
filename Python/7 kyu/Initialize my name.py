def initialize_names(name):
    name = name.split()

    return ' '.join(name) if len(name) < 3 else f"{name[0]} {'. '.join([name[i][0] for i in range(1, len(name) - 1)])}. {name[-1]}"
