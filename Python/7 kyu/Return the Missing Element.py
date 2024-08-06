def get_missing_element(seq):
    for i, n in enumerate(sorted(seq)):
        if i != n:
            return i
