def correct(str):
    for ch_1, ch_2 in {'0': 'O', '1': 'I', '5': 'S'}.items():
        str = str.replace(ch_1, ch_2)

    return str
