def kata_13_december(lst):
    j = 0
    for i in range(len(lst)):
        if lst[i - j] % 2 == 0:
            lst.remove(lst[i - j])
            j += 1
    return lst
