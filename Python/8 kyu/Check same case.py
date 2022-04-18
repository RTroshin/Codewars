def same_case (a, b):
    if not a.isalpha() or not b.isalpha():
        return -1
    else:
        return a.isupper() == b.isupper()
