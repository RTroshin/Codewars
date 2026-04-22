def even_last(numbers):
    res = []

    for i in range(len(numbers)):
        if not i % 2:
            res.append(numbers[i])

    return sum(res) * numbers[len(numbers) - 1]
