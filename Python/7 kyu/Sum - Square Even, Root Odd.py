def sum_square_even_root_odd(nums):
    return round(sum(i ** (1 / 2) if i % 2 else i ** 2 for i in nums), 2)
