def nickname_generator(name):
    if len(name) < 4:
        return "Error: Name too short"
    else:
        return name[:4] if name[2] in "aeiou" else name[:3]
