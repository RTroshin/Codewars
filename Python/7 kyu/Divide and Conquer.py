def div_con(arr):
    return sum(n for n in arr if isinstance(n, int)) - sum(int(n) for n in arr if isinstance(n, str))
