def nickname_generator(name):
    res = ''

    if len(name) < 4:
        res = "Error: Name too short"
    elif name[2] in "aeiou":
        res = name[:4]
    else:
        res = name[:3]

    return res
