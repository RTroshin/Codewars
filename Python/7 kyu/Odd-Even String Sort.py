def sort_my_string(s):
    return f"{''.join(s[i] for i in range(len(s)) if not i % 2)} {''.join(s[i] for i in range(len(s)) if i % 2)}"
