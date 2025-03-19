def sillycase(silly):
    lenSilly = len(silly)
    return ''.join(ch.lower() if i < lenSilly / 2 else ch.upper() for i, ch in enumerate(silly))
