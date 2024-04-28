def sort_my_string(str):
    return f"{''.join(str[i] for i in range(len(str)) if not i % 2)} {''.join(str[i] for i in range(len(str)) if i % 2)}"
