def string_clean(str):
    """
    Function will return the cleaned string
    """
    return ''.join(ch for ch in str if not ch.isdecimal())
