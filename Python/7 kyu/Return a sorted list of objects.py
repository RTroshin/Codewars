def sort_list(sort_by, lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if lst[j].get(sort_by) > lst[j + 1].get(sort_by):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst
