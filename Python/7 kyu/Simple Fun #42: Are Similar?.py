def are_similar(a, b):
    for i in range(len(a)):
        if b.count(a[i]) != a.count(a[i]):
            return False

    return True
