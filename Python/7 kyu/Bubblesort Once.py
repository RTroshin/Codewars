def bubblesort_once(l):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            tmp = l[i]
            l[i] = l[i + 1]
            l[i + 1] = tmp

    return l
