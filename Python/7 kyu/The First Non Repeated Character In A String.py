def first_non_repeated(str):
    return [ch for ch in str if str.count(ch) == 1][0]
