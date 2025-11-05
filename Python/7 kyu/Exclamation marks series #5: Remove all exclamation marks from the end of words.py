def remove(str):
    str = str.split()
    return ' '.join(s.rstrip('!') for s in str)
