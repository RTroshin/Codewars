def window(lngth, offst, lst):
    windows =[]

    for i in range(len(lst) - 1):
        wind = []

        for l in range(lngth):
            wind.append(lst[i])
            lst[i] += 1

        windows.append(wind)

    return windows
