def double_every_other(lst):
    return [n + n if i % 2 else n for i, n in enumerate(lst)]
