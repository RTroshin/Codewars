def sillycase(silly):
    res = []

    for i in range(len(silly)):
        if i < len(silly) // 2:
            res.append(silly[i].lower())
        else:
            res.append(silly[i].upper())

    res = ''.join(res)

    return res
