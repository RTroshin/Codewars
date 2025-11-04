def remove(str):
    str = str.split()
    return ' '.join(str[i].rstrip('!') for i in range(len(str)))
