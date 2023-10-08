def hello(*name):
    return f"Hello, {name[0].upper()[0]}{name[0].lower()[1:]}!" if name and name[0] else "Hello, World!"
