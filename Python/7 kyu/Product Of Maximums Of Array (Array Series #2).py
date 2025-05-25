def max_product(lst, n_largest_elements):
    max_prod = max(lst)
    max_lst = sorted(lst)[::-1]

    for i in range(1, n_largest_elements):
        max_prod *= max_lst[i]

    return max_prod
