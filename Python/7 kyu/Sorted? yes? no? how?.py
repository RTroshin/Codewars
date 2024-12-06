def is_sorted_and_how(arr):
    sortArr = sorted(arr)

    if arr == sortArr:
        return "yes, ascending"
    elif arr == sortArr[::-1]:
        return "yes, descending"
    else:
        return "no"
