def odd_ones_out(nums):
    return [n for n in nums if nums.count(n) % 2 == 0]
