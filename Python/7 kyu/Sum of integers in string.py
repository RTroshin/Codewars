def sum_of_integers_in_string(str):
    new_str = str

    for ch in str:
        if not ch.isdigit():
            new_str = ' '.join(new_str.split(ch))

    return sum(map(int, new_str.split()))
