def sillycase(silly):
    lenSilly = len(silly)
    res = [silly[i].lower() if i < lenSilly // 2 else silly[i].upper() for i in range(lenSilly)]

    return ''.join(res)
