def count(a, t, x):
    count = 0

    for i in range(len(a)):
        Add = Sub = a[i]
        if a[i] <= t:
            while Add < t:
                Add += x
                if Add == t:
                    count += 1
                    break
        else:
            while Sub > t:
                Sub -= x
                if Sub == t:
                    count += 1
                    break

    return count
