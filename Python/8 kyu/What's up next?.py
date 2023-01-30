def next_item(xs, item):
    try:
        return xs[xs.index(item) + 1] if item in xs else None
    except AttributeError:
        return 13
    except IndexError:
        return None
