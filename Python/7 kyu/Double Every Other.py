def double_every_other(lst):
    return [lst[i] + lst[i] if i % 2 else lst[i] for i in range(len(lst))]
