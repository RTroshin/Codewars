def enough(cap, on, wait):
    space = cap - on - wait
    return abs(space) if space < 0 else 0
