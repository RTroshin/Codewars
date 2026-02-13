def count(a, t, x):
    count = 0

    for i in range(len(a)):
        nAdd = nSub = a[i]
        if a[i] <= t:
            while nAdd < t:
                nAdd += x
                if nAdd == t:
                    count += 1
                    break
        else:
            while nSub > t:
                nSub -= x
                if nSub == t:
                    count += 1
                    break

    return count
