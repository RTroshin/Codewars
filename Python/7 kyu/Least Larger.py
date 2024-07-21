def least_larger(a, i):
    return a.index(min(a[j] for j in range(len(a)) if a[i] < a[j])) if a[i] != max(a) else -1
