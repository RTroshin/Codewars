def replace_all(obj, find, repl):
    tp = type(obj)

    if type(obj) == str:
        obj = obj.replace(find, repl)

    return obj if tp == str else len(obj) * [repl]
