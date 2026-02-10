def count(a, t, x):
    count = 0

    for i in range(len(a)):
        nAdd = a[i]
        nSub = a[i]
        while nAdd <= t or nSub > 0:
            nAdd += x
            nSub -= x
            if nAdd == x or nSub == x:
                count += 1
                break

    return count
