def hello(*name):
    return f"Hello, {name[0].capitalize()}!" if name and name[0] else "Hello, World!"
