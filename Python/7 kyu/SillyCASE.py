def sillycase(silly):
    lenSilly = len(silly)
    res = []

    for i in range(lenSilly):
        if i < lenSilly // 2:
            res.append(silly[i].lower())
        else:
            res.append(silly[i].upper())

    return ''.join(res)
