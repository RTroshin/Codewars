def max_product(lst, n_largest_elements):
    max_prod = 1
    lst.sort(reverse=True)

    for i in range(n_largest_elements):
        max_prod *= lst[i]

    return max_prod
