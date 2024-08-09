def replace_all(obj, find, repl):
    return obj.replace(find, repl) if type(obj) == str else [n if n != find else repl for n in obj]
