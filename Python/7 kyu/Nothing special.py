def nothing_special(st):
    if not isinstance(st, str):
        return "Not a string!"

    return ''.join(ch for ch in st if ch.isalpha() or ch.isdigit() or ch.isspace())
