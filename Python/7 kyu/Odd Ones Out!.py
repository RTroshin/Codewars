def odd_ones_out(nums):
    res = []

    for n in nums:
        if nums.count(n) % 2 == 0:
            res += [n]

    return res
