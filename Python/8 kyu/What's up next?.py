def next_item(xs, item):
    xs = iter(xs)
    try:
        while True:
            if next(xs) == item:
                return next(xs)
    except:
        return None
