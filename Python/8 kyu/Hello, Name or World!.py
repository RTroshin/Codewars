def hello(name):
    return "Hello, " + name.upper()[0] + name.lower()[1:] + '!' if name else "Hello, World!"
