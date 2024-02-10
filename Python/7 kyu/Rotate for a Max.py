def max_rot(n):
    n = str(n)
    arr = []

    for i in range(len(n)):
        n = n[:i] + n[i + 1:] + n[i]
        arr.append(int(n))

    return max(arr)
