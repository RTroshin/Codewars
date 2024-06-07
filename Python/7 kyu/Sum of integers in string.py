def sum_of_integers_in_string(str):
    new_str = ''

    for ch in str:
        if ch.isdigit():
            new_str += ch
        else:
            new_str += ' '

    return sum(map(int, new_str.split()))
