def tunnel_digging(r):
    time = 0

    for s in r:
        if s in "[]":
            time += 30
        elif s in "{}":
            time += 25
        elif s in "()":
            time += 20
        elif s in "|":
            time += 15
        elif s in ":":
            time += 10
    
    return time
