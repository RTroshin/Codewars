def find_missing_numbers(arr):
    return [i for i in range(arr[0], arr[-1]) if i not in arr] if len(arr) > 1 else []
