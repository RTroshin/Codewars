def century(year):
    return round(year / 100) if year / 100 <= round(year / 100) else round(year / 100) + 1
