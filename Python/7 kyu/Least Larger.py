def least_larger(a, i):
    return a.index(min(n for n in a if a[i] < n)) if a[i] != max(a) else -1
