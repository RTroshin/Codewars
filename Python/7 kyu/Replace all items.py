def replace_all(obj, find, repl):
    if type(obj) == str:
        obj = obj.replace(find, repl)

    return obj if type(obj) == str else len(obj) * [repl]
