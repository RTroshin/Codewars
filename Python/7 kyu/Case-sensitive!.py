def case_sensitive(s):
    return [s.islower() or False, [c for c in s if c.isupper()]]
