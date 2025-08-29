def window(lngth, offst, lst):
    windows =[]

    for i in range(len(lst) - 1):
        windows.append(lst[i: i + lngth])

    windowsRes = []

    for i in range(0, len(lst) - 1, offst):
        windowsRes.append(windows[i])
        

    return windowsRes
