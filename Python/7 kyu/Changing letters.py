def swap(str):
    return ''.join(v.upper() if v in "aeiou" else v for v in str)
