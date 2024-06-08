def sum_of_integers_in_string(str):
    new_str = ''

    for ch in str:
        new_str += ch if ch.isdigit() else ' '

    return sum(map(int, new_str.split()))
