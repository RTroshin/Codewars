def double_every_other(lst):
    return [n * 2 if i % 2 else n for i, n in enumerate(lst)]
