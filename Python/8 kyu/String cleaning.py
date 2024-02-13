def string_clean(str):
    return ''.join(ch for ch in str if not ch.isdecimal())
