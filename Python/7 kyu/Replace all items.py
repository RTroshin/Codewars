def replace_all(obj, find, repl):
    tp = type(obj)

    if type(obj) == str:
        obj = obj.replace(str(find), str(repl))

    return obj if tp == str else len(obj) * [repl]
