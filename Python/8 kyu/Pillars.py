def pillars(num_pill, dist, width):
    if num_pill == 2:
        return dist * 100
    elif num_pill > 2:
        return (num_pill - 1) * dist * 100 + (num_pill - 2) * width
    else:
        return 0
