def are_similar(a, b):
    for n in a:
        if b.count(n) != a.count(n):
            return False

    return True
