def swap(st):
    return ''.join([v.upper() if v in "aeiou" else v for v in st])
