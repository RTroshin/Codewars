def spacey(arr):
    return [f"{''.join(arr[:i])}{arr[i]}" for i in range(len(arr))]
