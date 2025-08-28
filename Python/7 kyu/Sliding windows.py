def window(lngth, offst, lst):
    windows =[]

    for i in range(len(lst) - 1):
        windows.append(lst[i: i + lngth])

    return windows
