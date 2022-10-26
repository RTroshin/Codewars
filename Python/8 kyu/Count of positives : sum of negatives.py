def count_positives_sum_negatives(arr):
    return [sum([1 for i in arr if i > 0]), sum([i for i in arr if i < 0])] if arr else []
