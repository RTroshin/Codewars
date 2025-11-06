def remove(str):
    return ' '.join(s.rstrip('!') for s in str.split())
