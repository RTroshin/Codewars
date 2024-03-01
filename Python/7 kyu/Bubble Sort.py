def bubble(lst):
    res_lst = []

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                tmp = lst[j + 1]
                lst[j + 1] = lst[j]
                lst[j] = tmp
                res_lst += [lst.copy()]

    return res_lst
