def max_product(lst, n_largest_elements):
    max_prod = 1
    max_lst = sorted(lst, reverse=True)

    for i in range(n_largest_elements):
        max_prod *= max_lst[i]

    return max_prod
