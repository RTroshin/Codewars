def least_larger(arr, i):
    return arr.index(min(n for n in arr if arr[i] < n)) if arr[i] != max(arr) else -1
