def even_chars(str):
    return [str[i] for i in range(1, len(str)) if i % 2] if 1 < len(str) < 101 else "invalid string"
