def process_data(data):
    mult = 1

    for n in [lst[0] - lst[1] for lst in data]:
        mult *= n

    return mult
