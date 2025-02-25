def sillycase(silly):
    lenSilly = len(silly)
    return ''.join(silly[i].lower() if i < lenSilly / 2 else silly[i].upper() for i in range(lenSilly))
