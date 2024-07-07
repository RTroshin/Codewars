def my_parse_int(str):
    str = str.strip()
    return int(str) if str.isdigit() else "NaN"
