def likes(names):
    lenNames = len(names)
    if lenNames < 2:
        return f"{names[0] if names else 'no one'} likes this"
    elif lenNames == 2:
        return f"{names[0]} and {names[1]} like this"
    elif lenNames == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {lenNames - 2} others like this"
