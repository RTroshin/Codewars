def kata_13_december(lst):
    lst = set(lst)
    for i in list(lst):
        if i % 2 == 0:
            lst.remove(i)
    return list(lst)
