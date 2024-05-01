def process_data(data):
    mult = 1

    for lst in data:
        mult *= lst[0] - lst[1]

    return mult
