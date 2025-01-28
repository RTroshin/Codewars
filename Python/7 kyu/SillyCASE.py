def sillycase(silly):
    lenSilly = len(silly)
    res = []

    for i in range(lenSilly):
        res.append(silly[i].lower()) if i < lenSilly // 2 else res.append(silly[i].upper())

    return ''.join(res)
