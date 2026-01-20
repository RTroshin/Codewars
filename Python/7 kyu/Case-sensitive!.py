def case_sensitive(str):
    res = [ch for ch in str if ch.isupper()]

    return [False, res] if res else [True, []]
