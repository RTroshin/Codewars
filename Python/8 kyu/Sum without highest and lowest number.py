def sum_array(arr):
    return sum(arr) - max(arr) - min(arr) if arr and len(arr[:3]) > 2 else 0
