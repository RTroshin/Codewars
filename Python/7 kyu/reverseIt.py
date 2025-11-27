def reverse_it(data):
    t = type(data)

    if t == str:
        return data[::-1]
    elif t == int:
        return int(str(data)[::-1])
    elif t == float:
        return float(str(data)[::-1])
    else:
        return data
