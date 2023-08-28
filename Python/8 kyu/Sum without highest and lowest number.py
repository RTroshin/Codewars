def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr[:3]) > 2 else 0
