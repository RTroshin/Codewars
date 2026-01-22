def case_sensitive(s):
    res = [c for c in s if c.isupper()]

    return [not res, res]
