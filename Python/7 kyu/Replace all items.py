def replace_all(obj, find, repl):
    if type(obj) != str:
        for i in range(len(obj)):
            if obj[i] == find:
                obj[i] = repl

    return obj.replace(find, repl) if type(obj) == str else obj
