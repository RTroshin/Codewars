def kata_13_december(lst):
    lst = set(lst)
    for i in list(lst):
        if not i % 2:
            lst.remove(i)
    return list(lst)
