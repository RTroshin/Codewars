def replace_all(obj, find, repl):
    tp = type(obj)

    if type(obj) != str:
        obj = ''.join(map(lambda i: str(i), obj))

    obj = obj.replace(str(find), str(repl))

    return obj if tp == str else list(map(lambda i: int(i), obj))
