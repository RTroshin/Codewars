def array(str):
    str = str.split(',')
    return ' '.join([str[i] for i in range(1, len(str) - 1)]) if len(str) > 2 else None
