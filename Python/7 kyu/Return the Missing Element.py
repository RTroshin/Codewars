def get_missing_element(seq):
    seq.sort()

    for i, n in enumerate(seq):
        if i != n:
            return i
