def tunnel_digging(r):
    time = 0

    for s in r:
        for c in s:
            if c in "[]":
                time += 30
            elif c in "{}":
                time += 25
            elif c in "()":
                time += 20
            elif c in "|":
                time += 15
            elif c in ":":
                time += 10
    
    return time
