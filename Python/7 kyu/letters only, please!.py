def remove_chars(str):
    return ''.join(ch for ch in str if ch.isalpha() or ch.isspace())
