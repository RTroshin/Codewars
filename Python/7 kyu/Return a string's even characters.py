def even_chars(str):
    return list(str[1::2]) if 1 < len(str) < 101 else "invalid string"
