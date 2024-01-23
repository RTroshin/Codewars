def only_duplicates(str):
    return ''.join(ch for ch in str if str.count(ch) > 1)
