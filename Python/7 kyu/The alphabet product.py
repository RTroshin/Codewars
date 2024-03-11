def alphabet(ns):
    sort_ns = sorted(ns)
    return sort_ns[7] / sort_ns[3 if sort_ns[0] * sort_ns[1] == sort_ns[2] else 2]
