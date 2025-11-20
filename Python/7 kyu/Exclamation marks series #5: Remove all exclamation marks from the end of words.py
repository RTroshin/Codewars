def remove(str):
    return ' '.join(s.rstrip('!') or s for s in str.split())
