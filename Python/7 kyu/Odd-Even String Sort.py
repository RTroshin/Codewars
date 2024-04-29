def sort_my_string(str):
    return f"{''.join(str[i] for i in range(0, len(str), 2))} {''.join(str[i] for i in range(1, len(str), 2))}"
