def nothing_special(st):
    return ''.join(ch for ch in st if ch.isalpha() or ch.isdigit() or ch.isspace()) if isinstance(st, str) else "Not a string!"
