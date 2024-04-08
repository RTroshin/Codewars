def eq_sum_powdig(h_max, exp):
    return [n for n in range(2, h_max + 1) if sum(int(i) ** exp for i in str(n)) == n]
