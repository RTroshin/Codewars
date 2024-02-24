def get_number_from_string(str):
    return int(''.join(ch for ch in str if ch.isdigit()))
