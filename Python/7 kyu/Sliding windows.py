def window(lngth, offst, lst):
    windows =[lst[i: i + lngth] for i in range(len(lst) - 1)]

    windowsRes = [windows[i] for i in range(0, len(lst) - 1, offst)]

    return windowsRes
