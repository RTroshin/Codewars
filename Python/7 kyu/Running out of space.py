def spacey(array):
    res = ['']

    for i in range(len(array)):
        res.append(f"{res[i]}{array[i]}")

    return res[1:]
