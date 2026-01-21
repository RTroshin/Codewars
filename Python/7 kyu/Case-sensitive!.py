def case_sensitive(str):
    res = [ch for ch in str if ch.isupper()]

    return [not res, res]
