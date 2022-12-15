def sum_no_duplicates(l):
    return sum([i for i in set(l) if l.count(i) == 1])
