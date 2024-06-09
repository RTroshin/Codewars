def sum_of_integers_in_string(str):
    return sum(map(int, ''.join([ch if ch.isdigit() else ' ' for ch in str]).split()))
