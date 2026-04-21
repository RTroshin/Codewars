def even_last(numbers):
    res = []

    for i in range(len(numbers)):
        if not i % 2:
            res.append(numbers[i])

    res = sum(res)

    return res * numbers[len(numbers) - 1]
