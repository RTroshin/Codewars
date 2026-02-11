def count(a, t, x):
    count = 0

    for i in range(len(a)):
        nAdd = a[i]
        nSub = a[i]
        while nAdd < t:
            nAdd += x
            if nAdd == t:
                count += 1
                break
        while nSub > t:
            nSub -= x
            if nSub == t:
                count += 1
                break

    return count
