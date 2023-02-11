def parse_float(str):
    try:
        return float(str)
    except ValueError:
        return None
